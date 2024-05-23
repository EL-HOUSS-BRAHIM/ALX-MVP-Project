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
# backend/database/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.init import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    expenses = relationship('Expense', back_populates='user')
    budget = relationship('Budget', uselist=False, back_populates='user')
    reminders = relationship('Reminder', back_populates='user')

    def __repr__(self):
        return f'<User {self.id}>'

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(120), nullable=False)
    date = Column(String(10), nullable=False)  # YYYY-MM-DD format

    user = relationship('User', back_populates='expenses')

    def __repr__(self):
        return f'<Expense {self.id}>'

class Budget(Base):
    __tablename__ = 'budgets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    amount = Column(Float, nullable=False)
    category = Column(String(120), nullable=False)
    period = Column(String(10), nullable=False)  # YYYY-MM format

    user = relationship('User', back_populates='budget')

    def __repr__(self):
        return f'<Budget {self.id}>'

class Reminder(Base):
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    due_date = Column(String(10), nullable=False)  # YYYY-MM-DD format

    user = relationship('User', back_populates='reminders')

    def __repr__(self):
        return f'<Reminder {self.id}>'
