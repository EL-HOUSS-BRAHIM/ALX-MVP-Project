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
from database.Reminder_DataB import ReminderDB


class ReminderModel:
    def __init__(self, db_path):
        self.db = ReminderDB(db_path)

    def _save(self, user_id, reminder_data):
        """
        Save a new reminder to the database.

        Args:
            user_id (str): The ID of the user.
            reminder_data (dict): The reminder data.

        Returns:
            str: The ID of the newly created reminder.
        """
        reminder_id = self.db._set_reminder(user_id, reminder_data)
        return str(reminder_id)

    def _delete(self, user_id, reminder_id):
        """
        Delete a reminder from the database.

        Args:
            user_id (str): The ID of the user.
            reminder_id (str): The ID of the reminder.

        Returns:
            bool: True if the reminder was deleted successfully, False otherwise.
        """
        return self.db._delete_reminder(user_id, reminder_id)
