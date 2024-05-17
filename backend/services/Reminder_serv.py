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
from models.Reminder_Mod import ReminderModel
from database.Reminder_DataB import ReminderDB
from middleware import InputValidator

class ReminderService:
    def __init__(self):
        self.model = ReminderModel()
        self.db = ReminderDB()
        self.validator = InputValidator()

    def set_reminder(self, user_id, reminder_data):
        """
        Set a new reminder.

        Args:
            user_id (str): The ID of the user.
            reminder_data (dict): The reminder data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and reminder data
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_reminder_data(reminder_data):
            return {"error": "Invalid reminder data"}

        # Set the reminder in the database
        reminder_id = self.model._save(user_id, reminder_data)

        # Return a success message
        return {"message": "Reminder set successfully", "reminder_id": reminder_id}

    def get_reminders(self, user_id):
        """
        Get all reminders for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: A list of reminders.
        """
        # Validate the user ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Get the reminders from the database
        reminders = self.db._get_reminders(user_id)

        # Return the list of reminders
        return reminders

    def delete_reminder(self, user_id, reminder_id):
        """
        Delete an existing reminder.

        Args:
            user_id (str): The ID of the user.
            reminder_id (str): The ID of the reminder.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and reminder ID
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_reminder_id(reminder_id):
            return {"error": "Invalid reminder ID"}

        # Delete the reminder from the database
        success = self.model._delete(user_id, reminder_id)

        # Return a success or error message
        if success:
            return {"message": "Reminder deleted successfully"}
        else:
            return {"error": "Failed to delete reminder"}