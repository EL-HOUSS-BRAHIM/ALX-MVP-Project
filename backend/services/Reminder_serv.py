#!/usr/bin/python3
from middleware.InpuValidat import InputValidator
from models.Reminder_Mod import ReminderModel
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


class ReminderService:


    def set_reminder(user_id, reminder_data):
        """
    Set a reminder for a user.

    Args:
        user_id (str): The ID of the user.
        reminder_data (dict): A dictionary containing reminder information (e.g., title, description, due_date).

    Returns:
        dict: A dictionary containing a success message.
    """
        try:
        # Validate the reminder data
            if not InputValidator.validate_reminder_input(reminder_data):
                return {"success": False, "message": "Invalid reminder data."}

        # Save the reminder data to the database
            reminder_model = ReminderModel()
            reminder_id = reminder_model._save(user_id, reminder_data)

            return {"success": True, "message": "Reminder set successfully.", "reminder_id": reminder_id}
        except Exception as e:
            return {"success": False, "message": f"Error setting reminder: {str(e)}"}


    def get_reminders(user_id):
        """
    Get a list of reminders for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: A list of dictionaries representing the user's reminders.
    """
        try:
        # Retrieve the user's reminders from the database
            reminder_model = ReminderModel()
            reminders = reminder_model._get_all(user_id)

            return reminders
        except Exception as e:
            return {"success": False, "message": f"Error getting reminders: {str(e)}"}

# services/ReminderService.py (continued)


    def delete_reminder(user_id, reminder_id):
        """
    Delete a reminder for a user.


    Args:
        user_id (str): The ID of the user.
        reminder_id (str): The ID of the reminder.

    Returns:
        dict: A dictionary containing a success message.
    """
        try:
        # Delete the reminder from the database
            reminder_model = ReminderModel()
            reminder_model._delete(user_id, reminder_id)

            return {"success": True, "message": "Reminder deleted successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error deleting reminder: {str(e)}"}
