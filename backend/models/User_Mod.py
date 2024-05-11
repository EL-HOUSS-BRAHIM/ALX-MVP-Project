#!/usr/bin/python3
from database.User_DataB import UserDB

user_db = UserDB()

class UserModel:
    def _save(self, email, username, hashed_password):
        """
        Save a new user to the database.
        """
        user_data = {
            'email': email,
            'username': username,
            'password': hashed_password
        }
        user = user_db._create_user(user_data)
        return user

    def _delete(self, user_id):
        """
        Delete a user from the database.
        """
        result = user_db._delete_user(user_id)
        return result

    def _update_profile(self, user_id, updated_data):
        """
        Update user profile details in the database.
        """
        result = user_db._update_user_profile(user_id, updated_data)
        return result
