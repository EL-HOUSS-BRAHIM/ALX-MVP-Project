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
from database.models import Reminder, User
from middleware import InputValidator

class ReminderService:
    def __init__(self):
        self.validator = InputValidator()

    def set_reminder(self, user_id, reminder_data):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        if not self.validator.validate_reminder_data(reminder_data):
            return {"error": "Invalid reminder data"}

        reminder = Reminder(
            user=user,
            title=reminder_data["title"],
            description=reminder_data.get("description"),
            due_date=reminder_data["due_date"],
        )
        session.add(reminder)
        session.commit()

        return {"message": "Reminder set successfully", "reminder_id": reminder.id}

    def get_reminders(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        reminders = user.reminders
        return [reminder.to_dict() for reminder in reminders]

    def delete_reminder(self, user_id, reminder_id):
        session = get_session()
        reminder = session.query(Reminder).filter_by(id=reminder_id, user_id=user_id).first()
        if not reminder:
            return {"error": "Reminder not found"}

        session.delete(reminder)
        session.commit()

        return {"message": "Reminder deleted successfully"}