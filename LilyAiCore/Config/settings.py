import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # dotenv is optional
    pass


def _bool(name: str, default: bool) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    discord_token: str
    groq_api_keys: tuple[str, ...]
    groq_base_url: str
    chat_model: str
    reasoning_model: str
    data_dir: Path
    log_level: str
    enable_discord: bool
    enable_api: bool
    api_host: str
    api_port: int
    admin_token: str
    cors_origins: tuple[str, ...]
    allowed_user_ids: frozenset[int]
    history_turns: int
    token_budget: int
    web_enabled: bool
    learn_from_chats: bool
    model_scan_enabled: bool
    model_scan_interval_hours: float
    model_scan_interval_s: float | None
    model_scan_max_auto: int
    model_scan_docs_dir: Path
    frontend_dir: str
    webhook_url: str
    umamoe_api_key: str
    umamoe_circle_ids: tuple[int, ...]
    umamoe_notify_user_id: str
    umamoe_poll_interval_hours: float
    umamoe_poll_interval_s: float | None
    turso_database_url: str
    turso_auth_token: str
    turso_sync_interval_s: float
    self_ping_enabled: bool
    self_ping_url: str
    self_ping_interval_s: float

    @property
    def db_path(self) -> Path:
        return self.data_dir / "lilyai.sqlite3"

    @property
    def model_scan_state_path(self) -> Path:
        return self.data_dir / "model_scan.json"

    @property
    def rag_path(self) -> Path:
        return self.data_dir / "rag_index.json"


def load_settings() -> Settings:
    data_dir = Path(os.getenv("LILYAI_DATA_DIR", "./data")).resolve()
    data_dir.mkdir(parents=True, exist_ok=True)
    allowed = frozenset(int(x) for x in os.getenv("ALLOWED_USER_IDS", "").split(",") if x.strip().isdigit())
    scan_seconds_raw = os.getenv("MODEL_SCAN_INTERVAL_SECONDS", "").strip()
    umamoe_seconds_raw = os.getenv("UMAMOE_POLL_INTERVAL_SECONDS", "").strip()
    return Settings(
        discord_token=os.getenv("DISCORD_TOKEN", ""),
        groq_api_keys=tuple(k.strip() for k in os.getenv("GROQ_API_KEY", "").split(",") if k.strip()),
        groq_base_url=os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
        chat_model=os.getenv("LILYAI_CHAT_MODEL", "openai/gpt-oss-20b"),
        reasoning_model=os.getenv("LILYAI_REASONING_MODEL", "openai/gpt-oss-120b"),
        data_dir=data_dir,
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        enable_discord=_bool("ENABLE_DISCORD", True),
        enable_api=_bool("ENABLE_API", True),
        api_host=os.getenv("API_HOST", "0.0.0.0"),
        api_port=int(os.getenv("PORT", os.getenv("API_PORT", "8000"))),
        admin_token=os.getenv("ADMIN_TOKEN", ""),
        cors_origins=tuple(o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()),
        allowed_user_ids=allowed,
        history_turns=int(os.getenv("HISTORY_TURNS", "12")),
        token_budget=int(os.getenv("TOKEN_BUDGET", "6000")),
        web_enabled=_bool("WEB_ENABLED", True),
        learn_from_chats=_bool("LEARN_FROM_CHATS", True),
        frontend_dir=os.getenv("FRONTEND_DIR", ""),
        model_scan_enabled=_bool("MODEL_SCAN_ENABLED", True),
        model_scan_interval_hours=float(os.getenv("MODEL_SCAN_INTERVAL_HOURS", "24")),
        model_scan_interval_s=float(scan_seconds_raw) if scan_seconds_raw else None,
        model_scan_max_auto=int(os.getenv("MODEL_SCAN_MAX_AUTO", "6")),
        model_scan_docs_dir=Path(os.getenv("MODEL_SCAN_DOCS_DIR", str(Path(__file__).resolve().parents[2] / "LilyAiGroqSupport"))),
        webhook_url=os.getenv("WEBHOOK_URL", ""),
        # uma.moe (Umamusume circle/fan tracking) - see LilyAiCore/ExternalServices/Umamoe/
        umamoe_api_key=os.getenv("UMAMOE_API_KEY", ""),
        umamoe_circle_ids=tuple(int(x) for x in os.getenv("UMAMOE_CIRCLE_IDS", "").split(",") if x.strip().isdigit()),
        # Discord user id to DM when a tracked circle's rank/points/fans change. Empty = log only.
        umamoe_notify_user_id=os.getenv("UMAMOE_NOTIFY_USER_ID", ""),
        umamoe_poll_interval_hours=float(os.getenv("UMAMOE_POLL_INTERVAL_HOURS", "6")),
        # Sub-hour override (e.g. 300 = every 5 minutes). Takes precedence over
        # UMAMOE_POLL_INTERVAL_HOURS when set. A 60s floor is enforced in bootstrap.py.
        umamoe_poll_interval_s=float(umamoe_seconds_raw) if umamoe_seconds_raw else None,
        # Turso (libSQL) - optional. When TURSO_DATABASE_URL is set, bootstrap.py uses
        # TursoDatabase (embedded replica) instead of local sqlite. See
        # LilyAiCore/ExternalServices/Database/turso.py.
        turso_database_url=os.getenv("TURSO_DATABASE_URL", ""),
        turso_auth_token=os.getenv("TURSO_AUTH_TOKEN", ""),
        turso_sync_interval_s=float(os.getenv("TURSO_SYNC_INTERVAL_SECONDS", "60")),
        # Self-ping (optional, on by default) - keeps a free-tier host (e.g. Render's free
        # plan) from sleeping the service after ~15 min of no inbound traffic, by hitting
        # its own /api/health on a schedule. Render auto-sets RENDER_EXTERNAL_URL, so this
        # needs no config there; SELF_PING_URL overrides it (e.g. for other hosts), and
        # SELF_PING_ENABLED=false turns it off entirely. See
        # LilyAiMain/MainService/Interaction/Workflows/self_ping_job.py.
        self_ping_enabled=_bool("SELF_PING_ENABLED", True),
        self_ping_url=os.getenv("SELF_PING_URL", os.getenv("RENDER_EXTERNAL_URL", "")),
        self_ping_interval_s=float(os.getenv("SELF_PING_INTERVAL_SECONDS", "300")),
    )
