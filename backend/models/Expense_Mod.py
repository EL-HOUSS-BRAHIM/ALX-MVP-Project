#!/usr/bin/python3
from database import Expense


class ExpenseModel:
    def __init__(self, db_path):
        self.db = Expense(db_path)

    def _save(self, user_id, expense_data):
        """
        Save a new expense to the database.

        Args:
            user_id (str): The ID of the user.
            expense_data (dict): The expense data.

        Returns:
            str: The ID of the newly created expense.
        """
        expense_id = self.db._add_expense(user_id, expense_data)
        return str(expense_id)

    def _delete(self, user_id, expense_id):
        """
        Delete an expense from the database.

        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.

        Returns:
            bool: True if the expense was deleted successfully, False otherwise.
        """
        return self.db._delete_expense(user_id, expense_id)

    def _update_details(self, user_id, expense_id, updated_data):
        """
        Update the details of an existing expense.

        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.
            updated_data (dict): The updated expense data.

        Returns:
            bool: True if the expense was updated successfully, False otherwise.
        """
        return self.db._update_expense(user_id, expense_id, updated_data)
