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
    groq_api_key: str
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
    model_scan_max_auto: int
    model_scan_docs_dir: Path
    frontend_dir: str

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
    return Settings(
        discord_token=os.getenv("DISCORD_TOKEN", ""),
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
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
        model_scan_max_auto=int(os.getenv("MODEL_SCAN_MAX_AUTO", "6")),
        model_scan_docs_dir=Path(os.getenv("MODEL_SCAN_DOCS_DIR", str(Path(__file__).resolve().parents[2] / "LilyAiGroqSupport"))),
    )
