import sqlite3
from datetime import datetime


class ReminderDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_reminders_table()

    def _create_reminders_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        )
        self.conn.commit()

    def _set_reminder(self, user_id, reminder_data):
        title = reminder_data["title"]
        description = reminder_data.get("description", "")
        due_date = reminder_data["due_date"]

        self.cursor.execute(
            """
            INSERT INTO reminders (user_id, title, description, due_date)
            VALUES (?, ?, ?, ?)
        """,
            (user_id, title, description, due_date),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def _get_reminders(self, user_id):
        self.cursor.execute(
            """
            SELECT id, title, description, due_date
            FROM reminders
            WHERE user_id = ?
        """,
            (user_id,),
        )
        reminders = self.cursor.fetchall()
        return [
            {
                "id": reminder[0],
                "title": reminder[1],
                "description": reminder[2],
                "due_date": reminder[3],
            }
            for reminder in reminders
        ]

    def _delete_reminder(self, user_id, reminder_id):
        self.cursor.execute(
            """
            DELETE FROM reminders
            WHERE user_id = ? AND id = ?
        """,
            (user_id, reminder_id),
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def __del__(self):
        self.conn.close()
