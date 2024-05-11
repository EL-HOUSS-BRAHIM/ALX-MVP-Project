#!/usr/bin/python3
from database import Reminder


class ReminderModel:
    def __init__(self, db_path):
        self.db = Reminder(db_path)

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
