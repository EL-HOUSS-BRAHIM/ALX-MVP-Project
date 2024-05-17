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
from database.models import User

class UserModel:
    def __init__(self, session):
        self.session = session

    def _save(self, user_data):
        email = user_data.get("email")
        username = user_data.get("username")
        password = user_data.get("password")

        existing_user = self.session.query(User).filter_by(email=email).first()
        if existing_user:
            return False

        new_user = User(email=email, username=username, password=password)
        self.session.add(new_user)
        self.session.commit()
        return True

    def _delete(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        self.session.delete(user)
        self.session.commit()
        return True

    def _update_profile(self, user_id, updated_data):
        user = self.session.query(User).filter_by(id=user_id).first()
        if not user:
            return False

        user.username = updated_data.get("username", user.username)
        self.session.commit()
        return True