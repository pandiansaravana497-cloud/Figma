"""
admin.py
Admin / management utilities — run directly to inspect data.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "db.sqlite3"


def list_registrations():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT r.id, r.full_name, r.email, e.name AS event, r.registered_at
        FROM registrations r
        JOIN events e ON e.id = r.event_id
        ORDER BY r.registered_at DESC
    """).fetchall()
    conn.close()

    if not rows:
        print("No registrations yet.")
        return

    print(f"\n{'ID':<5} {'Name':<25} {'Email':<30} {'Event':<25} {'Registered At'}")
    print("-" * 100)
    for r in rows:
        print(f"{r['id']:<5} {r['full_name']:<25} {r['email']:<30} {r['event']:<25} {r['registered_at']}")


def event_summary():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT e.name, e.max_participants,
               COUNT(r.id) AS registered
        FROM events e
        LEFT JOIN registrations r ON r.event_id = e.id
        GROUP BY e.id
    """).fetchall()
    conn.close()

    print(f"\n{'Event':<30} {'Max':<8} {'Registered':<12} {'Available'}")
    print("-" * 65)
    for r in rows:
        avail = r['max_participants'] - r['registered']
        print(f"{r['name']:<30} {r['max_participants']:<8} {r['registered']:<12} {avail}")


if __name__ == "__main__":
    print("=== Event Summary ===")
    event_summary()
    print("\n=== Registrations ===")
    list_registrations()
