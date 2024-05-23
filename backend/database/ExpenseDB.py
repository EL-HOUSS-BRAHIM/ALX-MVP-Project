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
# backend/database/ExpenseDB.py
from database.init import Session
from database.models import Expense

class ExpenseDB:
    """
    Expense database operations.
    """
    def _add_expense(self, user_id, expense_data):
        """
        Add a new expense for a user.
        

        Args:
            user_id (int): The ID of the user.
            expense_data (dict): A dictionary containing expense information.

        Returns:
            int: The ID of the newly added expense.
        """
        try:
            session = Session()
            expense = Expense(user_id=user_id, **expense_data)
            session.add(expense)
            session.commit()
            return expense.id
        except Exception as e:
            session.rollback()
            raise Exception(f"Error adding expense: {str(e)}")
        finally:
            session.close()

    def _get_expenses(self, user_id):
        """
        Get all expenses for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of dictionaries containing expense information.
        """
        try:
            session = Session()
            expenses = session.query(Expense).filter_by(user_id=user_id).all()
            expense_list = []
            for expense in expenses:
                expense_dict = {
                    "id": expense.id,
                    "amount": expense.amount,
                    "category": expense.category,
                    "date": expense.date,
                    # Add more fields as needed
                }
                expense_list.append(expense_dict)
            return expense_list
        except Exception as e:
            raise Exception(f"Error getting expenses: {str(e)}")
        finally:
            session.close()

    def _update_expense(self, user_id, expense_id, update_data):
        """
        Update an existing expense for a user.

        Args:
            user_id (int): The ID of the user.
            expense_id (int): The ID of the expense.
            update_data (dict): A dictionary containing the updated expense information.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        try:
            session = Session()
            expense = session.query(Expense).filter_by(user_id=user_id, id=expense_id).first()
            if expense:
                for key, value in update_data.items():
                    setattr(expense, key, value)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise Exception(f"Error updating expense: {str(e)}")
        finally:
            session.close()

    def _delete_expense(self, user_id, expense_id):
        """
        Delete an expense for a user.

        Args:
            user_id (int): The ID of the user.
            expense_id (int): The ID of the expense.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        try:
            session = Session()
            expense = session.query(Expense).filter_by(user_id=user_id, id=expense_id).first()
            if expense:
                session.delete(expense)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise Exception(f"Error deleting expense: {str(e)}")
        finally:
            session.close()
