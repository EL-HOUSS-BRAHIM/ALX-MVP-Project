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
from services.Expense_serv import ExpenseService


class ExpenseController:
    def __init__(self):
        self.service = ExpenseService()

    def add_expense(self, request):
        """
        Add a new expense.

        Args:
            request (dict): The request data containing the user ID and expense details.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        expense_data = request.get("expense_data")
        return self.service.add_expense(user_id, expense_data)

    def get_expenses(self, request):
        """
        Get all expenses for a user.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            list: A list of expenses.
        """
        user_id = request.get("user_id")
        return self.service.get_expenses(user_id)

    def update_expense(self, request):
        """
        Update an existing expense.

        Args:
            request (dict): The request data containing the user ID, expense ID, and updated expense details.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        expense_id = request.get("expense_id")
        updated_data = request.get("updated_data")
        return self.service.update_expense(user_id, expense_id, updated_data)

    def delete_expense(self, request):
        """
        Delete an existing expense.

        Args:
            request (dict): The request data containing the user ID and expense ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        expense_id = request.get("expense_id")
        return self.service.delete_expense(user_id, expense_id)
    def archive_expense(self, request):
        """
        Archive an existing expense.

        Args:
            request (dict): The request data containing the user ID and expense ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        expense_id = request.get("expense_id")
        return self.service.archive_expense(user_id, expense_id)