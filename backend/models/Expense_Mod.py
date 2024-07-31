#!/usr/bin/python3
import sys
import os
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.init_db import Base
from database.models import Budget, User
# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)
from database.models import Expense

class ExpenseModel:
    def __init__(self, session):
        self.session = session
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String)
    amount = Column(Float)
    date = Column(String)

    def _save(self, user_id, expense_data):
        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        expense = Expense(
            user=user,
            category=expense_data["category"],
            amount=expense_data["amount"],
            description=expense_data.get("description"),
        )
        self.session.add(expense)
        self.session.commit()
        return True

    def _delete(self, user_id, expense_id):
        expense = self.session.query(Expense).filter_by(id=expense_id, user_id=user_id).first()
        if not expense:
            return False

        self.session.delete(expense)
        self.session.commit()
        return True

    def _update_details(self, user_id, expense_id, updated_data):
        expense = self.session.query(Expense).filter_by(id=expense_id, user_id=user_id).first()
        if not expense:
            return False

        expense.category = updated_data["category"]
        expense.amount = updated_data["amount"]
        expense.description = updated_data.get("description")
        self.session.commit()
        return True