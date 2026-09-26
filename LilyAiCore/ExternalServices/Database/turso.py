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
        # The installed libsql_experimental build has no built-in periodic sync
        # (no sync_period kwarg on connect()), so background sync is driven here
        # with a plain threading.Timer instead.
        self._conn = libsql.connect(str(path), sync_url=sync_url, auth_token=auth_token)
        self._lock = threading.Lock()
        self._sync_interval_s = sync_interval_s
        self._timer: threading.Timer | None = None
        self.sync()
        if sync_interval_s:
            self._schedule_sync()

    def _schedule_sync(self) -> None:
        self._timer = threading.Timer(self._sync_interval_s, self._sync_and_reschedule)
        self._timer.daemon = True
        self._timer.start()

    def _sync_and_reschedule(self) -> None:
        try:
            self.sync()
        finally:
            if self._sync_interval_s:
                self._schedule_sync()

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
        if self._timer:
            self._timer.cancel()
        with self._lock:
            self._conn.close()
