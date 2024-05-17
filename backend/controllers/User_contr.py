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
from services.User_serv import UserService


class UserController:
    def __init__(self):
        self.service = UserService()

    def get_user_profile(self, request):
        """
        Get the user profile details.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: The user profile details or an error message.
        """
        user_id = request.get("user_id")
        return self.service.get_user_profile(user_id)

    def update_user_profile(self, request):
        """
        Update the user profile details.

        Args:
            request (dict): The request data containing the user ID and updated profile data.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        profile_data = request.get("profile_data")
        return self.service.update_user_profile(user_id, profile_data)

    def delete_user(self, request):
        """
        Delete a user account.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        return self.service.delete_user(user_id)
