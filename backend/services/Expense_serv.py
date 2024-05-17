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
from models.Expense_Mod import ExpenseModel
from database.Expense_DataB import ExpenseDB
from middleware import InpuValidat


class ExpenseService:
    def __init__(self):
        self.model = ExpenseModel()
        self.db = ExpenseDB()
        self.validator = InpuValidat()

    def add_expense(self, user_id, expense_data):
        """
        Add a new expense.

        Args:
            user_id (str): The ID of the user.
            expense_data (dict): The expense data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and expense data
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_expense_data(expense_data):
            return {"error": "Invalid expense data"}

        # Add the expense to the database
        expense_id = self.db._add_expense(user_id, expense_data)

        # If the expense was added successfully, return a success message
        if expense_id:
            return {"message": "Expense added successfully", "expense_id": expense_id}
        else:
            return {"error": "Failed to add expense"}

    def get_expenses(self, user_id):
        """
        Get all expenses for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of expenses.
        """
        # Validate the user ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Get the expenses from the database
        expenses = self.db._get_expenses(user_id)

        # Return the list of expenses
        return expenses

    def update_expense(self, user_id, expense_id, updated_data):
        """
        Update an existing expense.

        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.
            updated_data (dict): The updated expense data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID, expense ID, and updated data
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_expense_id(expense_id):
            return {"error": "Invalid expense ID"}
        if not self.validator.validate_expense_data(updated_data):
            return {"error": "Invalid expense data"}

        # Update the expense in the database
        success = self.model._update_details(user_id, expense_id, updated_data)

        # Return a success or error message
        if success:
            return {"message": "Expense updated successfully"}
        else:
            return {"error": "Failed to update expense"}

    def delete_expense(self, user_id, expense_id):
        """
        Delete an existing expense.

        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and expense ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_expense_id(expense_id):
            return {"error": "Invalid expense ID"}

        # Delete the expense from the database
        success = self.model._delete(user_id, expense_id)

        # Return a success or error message
        if success:
            return {"message": "Expense deleted successfully"}
        else:
            return {"error": "Failed to delete expense"}
