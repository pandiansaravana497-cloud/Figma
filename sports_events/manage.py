#!/usr/bin/env python
"""Sports Events Registration - Project Management CLI"""

import os
import sys
import argparse


def run_server(host="127.0.0.1", port=8000):
    """Start the development server."""
    import http.server
    import socketserver
    import webbrowser
    from pathlib import Path

    os.chdir(Path(__file__).parent)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/" or self.path == "":
                self.path = "/templates/index.html"
            elif self.path == "/events":
                self.path = "/templates/events.html"
            elif self.path == "/success":
                self.path = "/templates/success.html"
            return super().do_GET()

        def log_message(self, format, *args):
            print(f"  [SERVER] {self.address_string()} - {format % args}")

    print(f"\n  Sports Events Registration")
    print(f"  Server running at: http://{host}:{port}/")
    print(f"  Press CTRL+C to stop\n")

    with socketserver.TCPServer((host, port), Handler) as httpd:
        httpd.serve_forever()


def init_db():
    """Initialize the SQLite database with seed data."""
    import sqlite3
    from pathlib import Path

    db_path = Path(__file__).parent / "db.sqlite3"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            date       TEXT NOT NULL,
            venue      TEXT NOT NULL,
            category   TEXT NOT NULL,
            icon       TEXT NOT NULL,
            max_participants INTEGER DEFAULT 500
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name     TEXT NOT NULL,
            email         TEXT NOT NULL,
            event_id      INTEGER NOT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
    """)

    seed = [
        ("Marathon Championship", "December 15, 2025", "City Sports Complex",  "Running",    "🏃", 500),
        ("Basketball Tournament", "January 10, 2026",  "Downtown Arena",       "Basketball", "🏀",  16),
        ("Swimming Competition",  "December 28, 2025", "Olympic Pool Center",  "Swimming",   "🏊", 200),
        ("Football League",       "February 5, 2026",  "National Stadium",     "Football",   "⚽", 300),
        ("Tennis Open",           "March 12, 2026",    "Central Tennis Club",  "Tennis",     "🎾",  64),
    ]

    cur.execute("SELECT COUNT(*) FROM events")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO events (name, date, venue, category, icon, max_participants) VALUES (?,?,?,?,?,?)",
            seed
        )
        print("  Database seeded with 5 events.")
    else:
        print("  Database already initialised.")

    conn.commit()
    conn.close()
    print(f"  Database: {db_path}\n")


def main():
    parser = argparse.ArgumentParser(description="Sports Events Registration manage.py")
    subparsers = parser.add_subparsers(dest="command")

    srv = subparsers.add_parser("runserver", help="Start development server")
    srv.add_argument("--host", default="127.0.0.1")
    srv.add_argument("--port", type=int, default=8000)

    subparsers.add_parser("initdb", help="Initialise SQLite DB and seed events")

    args = parser.parse_args()

    if args.command == "runserver":
        run_server(args.host, args.port)
    elif args.command == "initdb":
        init_db()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
