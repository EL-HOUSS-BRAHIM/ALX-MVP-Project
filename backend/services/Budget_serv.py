#!/usr/bin/python3
import os
import sys

from middleware.InpuValidat import InputValidator
from models.Budget_Mod import BudgetModel

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)


class BudgetService:
    def set_budget(user_id, budget_data):
        """
        Set a budget for a user.

        Args:
            user_id (str): The ID of the user.
            budget_data (dict): A dictionary containing budget information (e.g., amount, category, period).

        Returns:
            dict: A dictionary containing a success message.
        """

        try:
            # Validate the budget data
            if not InputValidator.validate_budget_input(budget_data):
                return {"success": False, "message": "Invalid budget data."}

        # Save the budget data to the database
            budget_model = BudgetModel()
            budget_model._save(user_id, budget_data)

            return {"success": True, "message": "Budget set successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error setting budget: {str(e)}"}

    def get_budget_summary(user_id):
        """
        Get a summary of the user's budget.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing the user's budget summary.
        """
        try:
        # Retrieve the user's budget summary from the database
            budget_model = BudgetModel()
            budget_summary = budget_model._get_summary(user_id)

            if budget_summary:
                return budget_summary
            else:
                return {"success": False, "message": "Budget not found."}
        except Exception as e:
            return {"success": False, "message": f"Error getting budget summary: {str(e)}"}


    def update_budget(user_id, budget_data):
        """
        Update the user's budget.

        Args:
            user_id (str): The ID of the user.
            budget_data (dict): A dictionary containing the updated budget information.

        Returns:
            dict: A dictionary containing a success message.
        """
        try:
        # Validate the updated budget data
            if not InputValidator.validate_budget_input(budget_data):
                return {"success": False, "message": "Invalid budget data."}

        # Update the budget in the database
            budget_model = BudgetModel()
            budget_model._update(user_id, budget_data)

            return {"success": True, "message": "Budget updated successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error updating budget: {str(e)}"}


    def delete_budget(user_id):
        """
        Delete the user's budget.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing a success message.
        """
        try:
        # Delete the budget from the database
            budget_model = BudgetModel()
            budget_model._delete(user_id)

            return {"success": True, "message": "Budget deleted successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error deleting budget: {str(e)}"}
            return {"success": False, "message": f"Error deleting budget: {str(e)}"}