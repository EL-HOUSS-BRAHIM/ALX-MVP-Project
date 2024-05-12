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
from datetime import datetime
from database.connection import get_connection

class ExpenseDB:
    def create_expenses_table(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )
        db_connection.commit()
        cursor.close()

    def add_expense(self, user_id, expense_data):
        category = expense_data["category"]
        amount = expense_data["amount"]
        description = expense_data.get("description", "")
        date = datetime.now().strftime("%Y-%m-%d")
        query = """
            INSERT INTO expenses (user_id, category, amount, description, date)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (user_id, category, amount, description, date)
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, values)
            db_connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as error:
            print(f"Error adding expense: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def get_expenses(self, user_id):
        query = """
            SELECT id, category, amount, description, date
            FROM expenses
            WHERE user_id = %s
        """
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, (user_id,))
            expenses = cursor.fetchall()
            return [
                {
                    "id": expense[0],
                    "category": expense[1],
                    "amount": expense[2],
                    "description": expense[3],
                    "date": expense[4],
                }
                for expense in expenses
            ]
        except mysql.connector.Error as error:
            print(f"Error retrieving expenses: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def update_expense(self, user_id, expense_id, updated_data):
        category = updated_data.get("category")
        amount = updated_data.get("amount")
        description = updated_data.get("description")
        update_fields = []
        update_values = []
        if category:
            update_fields.append("category = %s")
            update_values.append(category)
        if amount:
            update_fields.append("amount = %s")
            update_values.append(amount)
        if description:
            update_fields.append("description = %s")
            update_values.append(description)
        update_values.append(user_id)
        update_values.append(expense_id)
        update_query = """
            UPDATE expenses
            SET {}
            WHERE user_id = %s AND id = %s
        """.format(", ".join(update_fields))
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(update_query, update_values)
            db_connection.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as error:
            print(f"Error updating expense: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def delete_expense(self, user_id, expense_id):
       query = """
           DELETE FROM expenses
           WHERE user_id = %s AND id = %s
       """
       try:
           db_connection = get_connection()
           cursor = db_connection.cursor()
           cursor.execute(query, (user_id, expense_id))
           db_connection.commit()
           return cursor.rowcount > 0
       except mysql.connector.Error as error:
           print(f"Error deleting expense: {error}")
           raise
       finally:
           if db_connection.is_connected():
               cursor.close()
               db_connection.close()