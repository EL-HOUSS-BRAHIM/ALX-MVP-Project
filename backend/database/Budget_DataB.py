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

class BudgetDB:
    def create_budgets_table(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )
        db_connection.commit()
        cursor.close()

    def set_budget(self, user_id, budget_data):
        amount = budget_data["amount"]
        category = budget_data["category"]
        start_date = budget_data["start_date"]
        end_date = budget_data["end_date"]
        query = """
            INSERT INTO budgets (user_id, amount, category, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (user_id, amount, category, start_date, end_date)
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, values)
            db_connection.commit()
            return cursor.lastrowid
        except mysql.connector.Error as error:
            print(f"Error setting budget: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def get_budget_summary(self, user_id):
        query = """
            SELECT amount, category, start_date, end_date
            FROM budgets
            WHERE user_id = %s
        """
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, (user_id,))
            budget = cursor.fetchone()
            if budget:
                return {
                    "amount": budget[0],
                    "category": budget[1],
                    "start_date": budget[2],
                    "end_date": budget[3],
                }
            return None
        except mysql.connector.Error as error:
            print(f"Error retrieving budget summary: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def update_budget(self, user_id, updated_data):
        amount = updated_data.get("amount")
        category = updated_data.get("category")
        start_date = updated_data.get("start_date")
        end_date = updated_data.get("end_date")
        update_fields = []
        update_values = []
        if amount:
            update_fields.append("amount = %s")
            update_values.append(amount)
        if category:
            update_fields.append("category = %s")
            update_values.append(category)
        if start_date:
            update_fields.append("start_date = %s")
            update_values.append(start_date)
        if end_date:
            update_fields.append("end_date = %s")
            update_values.append(end_date)
        update_values.append(user_id)
        update_query = """
            UPDATE budgets
            SET {}
            WHERE user_id = %s
        """.format(", ".join(update_fields))
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(update_query, update_values)
            db_connection.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as error:
            print(f"Error updating budget: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def delete_budget(self, user_id):
        query = """
            DELETE FROM budgets
            WHERE user_id = %s
        """
        try:
            db_connection = get_connection()
            cursor = db_connection.cursor()
            cursor.execute(query, (user_id,))
            db_connection.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as error:
            print(f"Error deleting budget: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()