#!/usr/bin/python3
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)
import sqlite3
from database.connection import get_connection

class ReminderDB:
    def create_reminders_table(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(
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
        db_connection.commit()
        cursor.close()

    def set_reminder(self, user_id, reminder_data):
        title = reminder_data["title"]
        description = reminder_data.get("description", "")
        due_date = reminder_data["due_date"]
        query = """
            INSERT INTO reminders (user_id, title, description, due_date)
            VALUES (%s, %s, %s, %s)
        """
        values = (user_id, title, description, due_date)
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, values)
            db_connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as error:
            print(f"Error setting reminder: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def get_reminders(self, user_id):
        query = """
            SELECT id, title, description, due_date
            FROM reminders
            WHERE user_id = %s
        """
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, (user_id,))
            reminders = cursor.fetchall()
            return [
                {
                    "id": reminder[0],
                    "title": reminder[1],
                    "description": reminder[2],
                    "due_date": reminder[3],
                }
                for reminder in reminders
            ]
        except mysql.connector.Error as error:
            print(f"Error retrieving reminders: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def delete_reminder(self, user_id, reminder_id):
       query = """
           DELETE FROM reminders
           WHERE user_id = %s AND id = %s
       """
       try:
           db_connection = get_connection()
           cursor = db_connection.cursor()
           cursor.execute(query, (user_id, reminder_id))
           db_connection.commit()
           return cursor.rowcount > 0
       except mysql.connector.Error as error:
           print(f"Error deleting reminder: {error}")
           raise
       finally:
           if db_connection.is_connected():
               cursor.close()
               db_connection.close()