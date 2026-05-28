"""
models.py
Data models for Events and Registrations.
Uses plain Python dataclasses + SQLite (no ORM dependency).
"""

import sqlite3
from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db.sqlite3"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@dataclass
class Event:
    id: int
    name: str
    date: str
    venue: str
    category: str
    icon: str
    max_participants: int

    @staticmethod
    def all() -> List["Event"]:
        with get_conn() as conn:
            rows = conn.execute("SELECT * FROM events ORDER BY id").fetchall()
        return [Event(**dict(r)) for r in rows]

    @staticmethod
    def get(event_id: int) -> Optional["Event"]:
        with get_conn() as conn:
            row = conn.execute("SELECT * FROM events WHERE id=?", (event_id,)).fetchone()
        return Event(**dict(row)) if row else None


@dataclass
class Registration:
    full_name: str
    email: str
    event_id: int
    id: int = 0
    registered_at: str = ""

    def save(self) -> int:
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO registrations (full_name, email, event_id) VALUES (?,?,?)",
                (self.full_name, self.email, self.event_id),
            )
            conn.commit()
            self.id = cur.lastrowid
        return self.id

    @staticmethod
    def count_for_event(event_id: int) -> int:
        with get_conn() as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM registrations WHERE event_id=?", (event_id,)
            ).fetchone()
        return row[0]
