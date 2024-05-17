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
from services.Budget_serv import BudgetService


class BudgetController:
    def __init__(self):
        self.service = BudgetService()

    def set_budget(self, request):
        """
        Set a new budget.

        Args:
            request (dict): The request data containing the user ID and budget details.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        budget_data = request.get("budget_data")
        return self.service.set_budget(user_id, budget_data)

    def get_budget_summary(self, request):
        """
        Get the budget summary for a user.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: The budget summary.
        """
        user_id = request.get("user_id")
        return self.service.get_budget_summary(user_id)

    def update_budget(self, request):
        """
        Update an existing budget.

        Args:
            request (dict): The request data containing the user ID and updated budget details.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        updated_data = request.get("updated_data")
        return self.service.update_budget(user_id, updated_data)

    def delete_budget(self, request):
        """
        Delete an existing budget.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        return self.service.delete_budget(user_id)
