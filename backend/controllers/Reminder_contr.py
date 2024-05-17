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
from services.Reminder_serv import ReminderService


class ReminderController:
    def __init__(self):
        self.service = ReminderService()

    def set_reminder(self, request):
        """
        Set a new reminder.

        Args:
            request (dict): The request data containing the user ID and reminder details.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        reminder_data = request.get("reminder_data")
        return self.service.set_reminder(user_id, reminder_data)

    def get_reminders(self, request):
        """
        Get all reminders for a user.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            list: A list of reminders.
        """
        user_id = request.get("user_id")
        return self.service.get_reminders(user_id)

    def delete_reminder(self, request):
        """
        Delete an existing reminder.

        Args:
            request (dict): The request data containing the user ID and reminder ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        reminder_id = request.get("reminder_id")
        return self.service.delete_reminder(user_id, reminder_id)
