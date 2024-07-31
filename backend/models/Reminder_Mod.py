#!/usr/bin/python3
import sys
import os
from sqlalchemy import Column, Integer, String, ForeignKey
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
from database.models import Reminder
from database.models import Budget, User
class ReminderModel:
    def __init__(self, session):
        self.session = session
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String)
    date = Column(String)

    def _save(self, user_id, reminder_data):
        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        reminder = Reminder(
            user=user,
            title=reminder_data["title"],
            description=reminder_data.get("description"),
            due_date=reminder_data["due_date"],
        )
        self.session.add(reminder)
        self.session.commit()
        return True

    def _delete(self, user_id, reminder_id):
        reminder = self.session.query(Reminder).filter_by(id=reminder_id, user_id=user_id).first()
        if not reminder:
            return False

        self.session.delete(reminder)
        self.session.commit()
        return True