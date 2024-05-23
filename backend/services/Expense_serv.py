#!/usr/bin/python3
from middleware.InpuValidat import InputValidator
from models.Expense_Mod import ExpenseModel
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


class ExpenseService:
    def add_expense(user_id, expense_data):
        """
            Add a new expense for a user.

            Args:
                user_id (str): The ID of the user.
                expense_data (dict): A dictionary containing expense information (e.g., amount, category, date).

            Returns:
                dict: A dictionary containing a success message.
        """
        try:
       # Validate the expense data
            if not InputValidator.validate_expense_input(expense_data):
                return {"success": False, "message": "Invalid expense data."}

       # Save the expense data to the database
            expense_model = ExpenseModel()
            expense_id = expense_model._save(user_id, expense_data)

            return {"success": True, "message": "Expense added successfully.", "expense_id": expense_id}
        except Exception as e:
            return {"success": False, "message": f"Error adding expense: {str(e)}"}

    def get_expenses(user_id):
        """
        Get a list of expenses for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of dictionaries representing the user's expenses.
        """
        try:
       # Retrieve the user's expenses from the database
            expense_model = ExpenseModel()
            expenses = expense_model._get_all(user_id)

            return expenses
        except Exception as e:
            return {"success": False, "message": f"Error getting expenses: {str(e)}"}

    def update_expense(user_id, expense_id, update_data):
        """
        Update an existing expense for a user.

        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.
            update_data (dict): A dictionary containing the updated expense information.

        Returns:
            dict: A dictionary containing a success message.
        """
        try:
       # Validate the updated expense data
            if not InputValidator.validate_expense_input(update_data):
                return {"success": False, "message": "Invalid expense data."}

       # Update the expense in the database
            expense_model = ExpenseModel()
            expense_model._update_details(user_id, expense_id, update_data)

            return {"success": True, "message": "Expense updated successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error updating expense: {str(e)}"}

    def delete_expense(user_id, expense_id):
        """
        Delete an expense for a user.


        Args:
            user_id (str): The ID of the user.
            expense_id (str): The ID of the expense.

        Returns:
            dict: A dictionary containing a success message.
        """
        try:
       # Delete the expense from the database
            expense_model = ExpenseModel()
            expense_model._delete(user_id, expense_id)

            return {"success": True, "message": "Expense deleted successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error deleting expense: {str(e)}"}