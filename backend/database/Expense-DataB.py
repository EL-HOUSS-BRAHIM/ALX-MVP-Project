import sqlite3
from datetime import datetime


class ExpenseDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_expenses_table()

    def _create_expenses_table(self):
        self.cursor.execute(
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
        self.conn.commit()

    def _add_expense(self, user_id, expense_data):
        category = expense_data["category"]
        amount = expense_data["amount"]
        description = expense_data.get("description", "")
        date = datetime.now().strftime("%Y-%m-%d")

        self.cursor.execute(
            """
            INSERT INTO expenses (user_id, category, amount, description, date)
            VALUES (?, ?, ?, ?, ?)
        """,
            (user_id, category, amount, description, date),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def _get_expenses(self, user_id):
        self.cursor.execute(
            """
            SELECT id, category, amount, description, date
            FROM expenses
            WHERE user_id = ?
        """,
            (user_id,),
        )
        expenses = self.cursor.fetchall()
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

    def _update_expense(self, user_id, expense_id, updated_data):
        category = updated_data.get("category")
        amount = updated_data.get("amount")
        description = updated_data.get("description")

        update_fields = []
        update_values = []

        if category:
            update_fields.append("category = ?")
            update_values.append(category)
        if amount:
            update_fields.append("amount = ?")
            update_values.append(amount)
        if description:
            update_fields.append("description = ?")
            update_values.append(description)

        update_values.append(user_id)
        update_values.append(expense_id)

        update_query = """
            UPDATE expenses
            SET {}
            WHERE user_id = ? AND id = ?
        """.format(
            ", ".join(update_fields)
        )

        self.cursor.execute(update_query, update_values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def _delete_expense(self, user_id, expense_id):
        self.cursor.execute(
            """
            DELETE FROM expenses
            WHERE user_id = ? AND id = ?
        """,
            (user_id, expense_id),
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def __del__(self):
        self.conn.close()
