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
from database.connection import get_session
from database.models import Budget, User
from middleware import InputValidator

class BudgetService:
    def __init__(self):
        self.validator = InputValidator()

    def set_budget(self, user_id, budget_data):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        if not self.validator.validate_budget_data(budget_data):
            return {"error": "Invalid budget data"}

        budget = Budget(
            user=user,
            amount=budget_data["amount"],
            category=budget_data["category"],
            start_date=budget_data["start_date"],
            end_date=budget_data["end_date"],
        )
        session.add(budget)
        session.commit()

        return {"message": "Budget set successfully"}

    def get_budget_summary(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        budgets = user.budgets
        budget_summary = [budget.to_dict() for budget in budgets]
        return budget_summary

    def update_budget(self, user_id, updated_data):
        session = get_session()
        budget = session.query(Budget).filter_by(user_id=user_id).first()
        if not budget:
            return {"error": "Budget not found"}

        if not self.validator.validate_budget_data(updated_data):
            return {"error": "Invalid budget data"}

        budget.amount = updated_data["amount"]
        budget.category = updated_data["category"]
        budget.start_date = updated_data["start_date"]
        budget.end_date = updated_data["end_date"]
        session.commit()

        return {"message": "Budget updated successfully"}

    def delete_budget(self, user_id):
        session = get_session()
        budget = session.query(Budget).filter_by(user_id=user_id).first()
        if not budget:
            return {"error": "Budget not found"}

        session.delete(budget)
        session.commit()

        return {"message": "Budget deleted successfully"}