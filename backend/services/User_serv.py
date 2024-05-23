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
from models.User_Mod import UserModel
from middleware.InpuValidat import InputValidator
class UserService:
    def get_user_profile(user_id):
        """
        Get a user's profile information.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing the user's profile information.
        """
        try:
        # Retrieve the user's profile from the database
            user_model = UserModel()
            user_profile = user_model._get_profile(user_id)

            if user_profile:
                return user_profile
            else:
                return {"success": False, "message": "User not found."}
        except Exception as e:
            return {"success": False, "message": f"Error getting user profile: {str(e)}"}

    def update_user_profile(user_id, update_data):
        """
    Update a user's profile information.

    Args:
        user_id (str): The ID of the user.
        update_data (dict): A dictionary containing the updated profile information.

    Returns:
        dict: A dictionary containing a success message.
    """
        try:
        # Validate the updated user data
            if not InputValidator.validate_user_input(update_data):
                return {"success": False, "message": "Invalid user data."}

        # Update the user's profile in the database
            user_model = UserModel()
            user_model._update_profile(user_id, update_data)

            return {"success": True, "message": "User profile updated successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error updating user profile: {str(e)}"}

    def delete_user(user_id):
        """
    Delete a user account.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: A dictionary containing a success message.
    """
        try:
        # Delete the user from the database
            user_model = UserModel()
            user_model._delete(user_id)

            return {"success": True, "message": "User deleted successfully."}
        except Exception as e:
            return {"success": False, "message": f"Error deleting user: {str(e)}"}

    def track_login_attempts(user_id):
        """
    Track the number of login attempts for a user.


    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: A dictionary containing the login attempt count and a success message.
    """
        try:
        # Retrieve the login attempt count from the database (not implemented here)
        # ...
            login_attempts = 3

            return {"success": True, "login_attempts": login_attempts}
        except Exception as e:
            return {"success": False, "message": f"Error tracking login attempts: {str(e)}"}