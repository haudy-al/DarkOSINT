import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS leaks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                value TEXT,
                source TEXT
            )
        """)

    def save_leak(self, leak_type, value, source):
        self.conn.execute("INSERT INTO leaks (type, value, source) VALUES (?, ?, ?)",
                          (leak_type, value, source))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT type, value, source FROM leaks")
        return cursor.fetchall()
