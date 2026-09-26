"""Turso (libSQL) database adapter.

Same call surface as ExternalServices.Database.sqlite.Database
(execute/executescript/query/query_one/close), so this is a drop-in swap
for any domain that only depends on the Database interface — nothing in
LilyAiMemory or elsewhere needs to change to use it.

Uses an embedded replica: a local libSQL file that syncs against the
remote Turso primary. Reads hit the local file (fast, works even if the
network is briefly down); writes go through and replicate on the next
sync() call.
"""
import threading
from pathlib import Path
from typing import Any, Iterable

import libsql_experimental as libsql


class TursoDatabase:
    def __init__(
        self,
        path: str | Path,
        sync_url: str,
        auth_token: str,
        sync_interval_s: float | None = 60.0,
    ):
        # sync_period enables background auto-sync on this interval, in addition to
        # the explicit sync() call below on startup so the replica is never stale
        # right after a cold start (e.g. right after a redeploy).
        self._conn = libsql.connect(
            str(path), sync_url=sync_url, auth_token=auth_token, sync_period=sync_interval_s
        )
        self._lock = threading.Lock()
        self.sync()

    def sync(self) -> None:
        with self._lock:
            self._conn.sync()

    def execute(self, sql: str, params: Iterable[Any] = ()) -> int:
        with self._lock:
            cur = self._conn.execute(sql, tuple(params))
            self._conn.commit()
            return cur.lastrowid or 0

    def executescript(self, script: str) -> None:
        # libsql_experimental doesn't expose sqlite3's executescript, so run each
        # statement individually. Schemas here are plain CREATE TABLE/INDEX
        # statements with no string literals containing ';', so a naive split is safe.
        with self._lock:
            for statement in filter(None, (s.strip() for s in script.split(";"))):
                self._conn.execute(statement)
            self._conn.commit()

    def query(self, sql: str, params: Iterable[Any] = ()) -> list[dict[str, Any]]:
        with self._lock:
            cur = self._conn.execute(sql, tuple(params))
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

    def query_one(self, sql: str, params: Iterable[Any] = ()) -> dict[str, Any] | None:
        rows = self.query(sql, params)
        return rows[0] if rows else None

    def close(self) -> None:
        with self._lock:
            self._conn.close()
