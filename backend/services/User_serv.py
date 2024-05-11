#!/usr/bin/python3
from models.User_Mod import UserModel
from database.User_DataB import UserDB
from middleware import InpuValidat, Promise





class UserService:
    def __init__(self):
        self.model = UserModel()
        self.db = UserDB()
        self.validator = InpuValidat()

    def get_user_profile(self, user_id):
        """
        Get the user profile details.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: The user profile details.
        """
        # Validate the user ID input
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Retrieve the user profile from the database
        user_profile = self.db._get_user_profile(user_id)

        # If the user profile is not found, return an error
        if not user_profile:
            return {"error": "User not found"}

        # Return the user profile
        return user_profile

    def update_user_profile(self, user_id, profile_data):
        """
        Update the user profile details.

        Args:
            user_id (str): The ID of the user.
            profile_data (dict): The updated profile data.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID and profile data input
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}
        if not self.validator.validate_user_profile(profile_data):
            return {"error": "Invalid profile data"}

        # Update the user profile in the database
        success = self.model._update_profile(user_id, profile_data)

        # Return a success or error message
        if success:
            return {"message": "User profile updated successfully"}
        else:
            return {"error": "Failed to update user profile"}

    def delete_user(self, user_id):
        """
        Delete a user account.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A success or error message.
        """
        # Validate the user ID input
        if not self.validator.validate_user_id(user_id):
            return {"error": "Invalid user ID"}

        # Delete the user from the database
        success = self.model._delete(user_id)

        # Return a success or error message
        if success:
            return {"message": "User account deleted successfully"}
        else:
            return {"error": "Failed to delete user account"}

    def track_login_attempts(self, user_id):
        """
        Track the number of login attempts for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            Promise: A promise that resolves with the updated login attempt count.
        """
        # Validate the user ID input
        validation_promise = self.validator.validate_user_id(user_id)

        def handle_validation_result(is_valid):
            if is_valid:
                # Track the login attempt in the database
                updated_attempts = self.db._track_login_attempt(user_id)
                return Promise.resolve(updated_attempts)
            else:
                return Promise.reject("Invalid user ID")

        return validation_promise.then(handle_validation_result)
