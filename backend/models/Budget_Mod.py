#!/usr/bin/python3
import sys
import os
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.init_db import Base

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)
from database.models import Budget, User

class BudgetModel:
    def __init__(self, session):
        self.session = session
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String)
    amount = Column(Float)

    def _save(self, user_id, budget_data):
        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        budget = Budget(
            user=user,
            amount=budget_data["amount"],
            category=budget_data["category"],
            start_date=budget_data["start_date"],
            end_date=budget_data["end_date"],
        )
        self.session.add(budget)
        self.session.commit()
        return True

    def _delete(self, user_id):
        budget = self.session.query(Budget).filter_by(user_id=user_id).first()
        if not budget:
            return False

        self.session.delete(budget)
        self.session.commit()
        return True