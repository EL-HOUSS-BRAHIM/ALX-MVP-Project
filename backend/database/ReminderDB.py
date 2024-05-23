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
# backend/database/ReminderDB.py
from database.init import Session
from database.models import Reminder

class ReminderDB:
    """
    Reminder database operations.
    """
    def _add_reminder(self, user_id, reminder_data):
        """
        Add a new reminder for a user.

        Args:
            user_id (int): The ID of the user.
            reminder_data (dict): A dictionary containing reminder information.

        Returns:
            int: The ID of the newly added reminder.
        """
        try:
            session = Session()
            reminder = Reminder(user_id=user_id, **reminder_data)
            session.add(reminder)
            session.commit()
            return reminder.id
        except Exception as e:
            session.rollback()
            raise Exception(f"Error adding reminder: {str(e)}")
        finally:
            session.close()

    def _get_reminders(self, user_id):
        """
        Get all reminders for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of dictionaries containing reminder information.
        """
        try:
            session = Session()
            reminders = session.query(Reminder).filter_by(user_id=user_id).all()
            reminder_list = []
            for reminder in reminders:
                reminder_dict = {
                    "id": reminder.id,
                    "title": reminder.title,
                    "description": reminder.description,
                    "due_date": reminder.due_date,
                    # Add more fields as needed
                }
                reminder_list.append(reminder_dict)
            return reminder_list
        except Exception as e:
            raise Exception(f"Error getting reminders: {str(e)}")
        finally:
            session.close()

    def _delete_reminder(self, user_id, reminder_id):
        """
        Delete a reminder for a user.

        Args:
            user_id (int): The ID of the user.
            reminder_id (int): The ID of the reminder.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        try:
            session = Session()
            reminder = session.query(Reminder).filter_by(user_id=user_id, id=reminder_id).first()
            if reminder:
                session.delete(reminder)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise Exception(f"Error deleting reminder: {str(e)}")
        finally:
            session.close()
