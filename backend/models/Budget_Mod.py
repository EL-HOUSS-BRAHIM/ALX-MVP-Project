#!/usr/bin/python3
from database.Budget_DataB import BudgetDB


class BudgetModel:
    def __init__(self, db_path):
        self.db = BudgetDB(db_path)

    def _save(self, user_id, budget_data):
        """
        Save a new budget to the database.

        Args:
            user_id (str): The ID of the user.
            budget_data (dict): The budget data.

        Returns:
            bool: True if the budget was saved successfully, False otherwise.
        """
        budget_id = self.db._set_budget(user_id, budget_data)
        return bool(budget_id)

    def _delete(self, user_id):
        """
        Delete a budget from the database.

        Args:
            user_id (str): The ID of the user.

        Returns:
            bool: True if the budget was deleted successfully, False otherwise.
        """
        return self.db._delete_budget(user_id)
