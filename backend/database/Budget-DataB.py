import sqlite3
from datetime import datetime


class BudgetDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_budgets_table()

    def _create_budgets_table(self):
        self.cursor.execute(
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
        self.conn.commit()

    def _set_budget(self, user_id, budget_data):
        amount = budget_data["amount"]
        category = budget_data["category"]
        start_date = budget_data["start_date"]
        end_date = budget_data["end_date"]

        self.cursor.execute(
            """
            INSERT INTO budgets (user_id, amount, category, start_date, end_date)
            VALUES (?, ?, ?, ?, ?)
        """,
            (user_id, amount, category, start_date, end_date),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def _get_budget_summary(self, user_id):
        self.cursor.execute(
            """
            SELECT amount, category, start_date, end_date
            FROM budgets
            WHERE user_id = ?
        """,
            (user_id,),
        )
        budget = self.cursor.fetchone()
        if budget:
            return {
                "amount": budget[0],
                "category": budget[1],
                "start_date": budget[2],
                "end_date": budget[3],
            }
        return None

    def _update_budget(self, user_id, updated_data):
        amount = updated_data.get("amount")
        category = updated_data.get("category")
        start_date = updated_data.get("start_date")
        end_date = updated_data.get("end_date")

        update_fields = []
        update_values = []

        if amount:
            update_fields.append("amount = ?")
            update_values.append(amount)
        if category:
            update_fields.append("category = ?")
            update_values.append(category)
        if start_date:
            update_fields.append("start_date = ?")
            update_values.append(start_date)
        if end_date:
            update_fields.append("end_date = ?")
            update_values.append(end_date)

        update_values.append(user_id)

        update_query = """
            UPDATE budgets
            SET {}
            WHERE user_id = ?
        """.format(
            ", ".join(update_fields)
        )

        self.cursor.execute(update_query, update_values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def _delete_budget(self, user_id):
        self.cursor.execute(
            """
            DELETE FROM budgets
            WHERE user_id = ?
        """,
            (user_id,),
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def __del__(self):
        self.conn.close()
