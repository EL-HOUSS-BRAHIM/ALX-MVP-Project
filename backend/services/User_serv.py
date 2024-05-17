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
from database.connection import get_session
from database.models import User
from middleware import InputValidator, Promise

class UserService:
    def __init__(self):
        self.validator = InputValidator()

    def get_user_profile(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "User not found"}

        return user.to_dict()

    def update_user_profile(self, user_id, profile_data):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "User not found"}

        if not self.validator.validate_user_profile(profile_data):
            return {"error": "Invalid profile data"}

        user.username = profile_data.get("username", user.username)
        session.commit()

        return {"message": "User profile updated successfully"}

    def delete_user(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "User not found"}

        session.delete(user)
        session.commit()

        return {"message": "User account deleted successfully"}

    def track_login_attempts(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return Promise.reject("Invalid user ID")

        user.login_attempts += 1
        session.commit()

        return Promise.resolve(user.login_attempts)