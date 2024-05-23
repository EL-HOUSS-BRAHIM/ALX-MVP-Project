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
# backend/database/BudgetDB.py
from database.init import Session
from database.models import Budget


class BudgetDB:
    """
    Budget database operations.
    """
    def _set_budget(self, user_id, budget_data):
        """
        Set or update budget for a user.

        Args:
            user_id (int): The ID of the user.
            budget_data (dict): A dictionary containing budget information.

        Returns:
            bool: True if the budget was set successfully, False otherwise.
        """
        try:
            session = Session()
            budget = session.query(Budget).filter_by(user_id=user_id).first()
            if budget:
                for key, value in budget_data.items():
                    setattr(budget, key, value)
            else:
                budget = Budget(user_id=user_id, **budget_data)
                session.add(budget)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise Exception(f"Error setting budget: {str(e)}")
        finally:
            session.close()

    def _get_budget(self, user_id):
        """
        Get budget for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict: A dictionary containing budget information.
        """
        try:
            session = Session()
            budget = session.query(Budget).filter_by(user_id=user_id).first()
            if budget:
                return {
                    "id": budget.id,
                    "user_id": budget.user_id,
                    "amount": budget.amount,
                    "category": budget.category,
                    "period": budget.period,
                    # Add more fields as needed
                }
            else:
                return None
        except Exception as e:
            raise Exception(f"Error getting budget: {str(e)}")
        finally:
            session.close()
