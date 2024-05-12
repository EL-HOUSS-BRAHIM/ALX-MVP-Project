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
from models.Budget_Mod import BudgetModel
from database.Budget_DataB import BudgetDB
from middleware import InputValidator

class BudgetService:
    def __init__(self):
        self.model = BudgetModel()
        self.db = BudgetDB()
        self.validator = InputValidator()

    def set_budget(self, user_id, budget_data):
        """
        Set a new budget.

        Args:
            user_id (str): The ID of the user.
            budget_data (dict): The budget data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and budget data
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_budget_data(budget_data):
            return {"error": "Invalid budget data"}

        # Set the budget in the database
        success = self.model._save(user_id, budget_data)

        # Return a success or error message
        if success:
            return {"message": "Budget set successfully"}
        else:
            return {"error": "Failed to set budget"}

    def get_budget_summary(self, user_id):
        """
        Get the budget summary for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: The budget summary.
        """
        # Validate the user ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Get the budget summary from the database
        budget_summary = self.db._get_budget_summary(user_id)

        # Return the budget summary
        return budget_summary

    def update_budget(self, user_id, updated_data):
        """
        Update an existing budget.

        Args:
            user_id (str): The ID of the user.
            updated_data (dict): The updated budget data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and updated data
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_budget_data(updated_data):
            return {"error": "Invalid budget data"}

        # Update the budget in the database
        success = self.model._update(user_id, updated_data)

        # Return a success or error message
        if success:
            return {"message": "Budget updated successfully"}
        else:
            return {"error": "Failed to update budget"}

    def delete_budget(self, user_id):
        """
        Delete an existing budget.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Delete the budget from the database
        success = self.model._delete(user_id)

        # Return a success or error message
        if success:
            return {"message": "Budget deleted successfully"}
        else:
            return {"error": "Failed to delete budget"}