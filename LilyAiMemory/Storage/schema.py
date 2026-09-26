SCHEMA = """
CREATE TABLE IF NOT EXISTS user_facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    fact TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'user',
    created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_user_facts_user ON user_facts(user_id);

CREATE TABLE IF NOT EXISTS conversation_turns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_turns_user ON conversation_turns(user_id, id);

CREATE TABLE IF NOT EXISTS trainer_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id TEXT NOT NULL UNIQUE,
    trainer_id TEXT NOT NULL UNIQUE,
    trainer_name TEXT,
    created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_trainer_links_trainer ON trainer_links(trainer_id);

CREATE TABLE IF NOT EXISTS fan_snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club TEXT NOT NULL,
    trainer_id TEXT NOT NULL,
    fan_total INTEGER NOT NULL,
    snapshot_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_fan_snapshots_lookup ON fan_snapshots(club, trainer_id, snapshot_at);

CREATE TABLE IF NOT EXISTS deficit_tracker_state (
    club TEXT NOT NULL,
    trainer_id TEXT NOT NULL,
    carry INTEGER NOT NULL DEFAULT 0,
    total_gained INTEGER NOT NULL DEFAULT 0,
    updated_at REAL,
    PRIMARY KEY (club, trainer_id)
);

CREATE TABLE IF NOT EXISTS daily_job_runs (
    job_name TEXT NOT NULL,
    run_date TEXT NOT NULL,
    ran_at REAL,
    PRIMARY KEY (job_name, run_date)
);
"""
