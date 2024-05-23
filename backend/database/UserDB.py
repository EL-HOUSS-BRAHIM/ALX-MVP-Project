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
# backend/database/UserDB.py
from database.init import Session
from database.models import User

class UserDB:
    """
    User database operations.
    """
    def _create_user(self, user_data):
        """
        Create a new user.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            int: The ID of the newly created user.
        """
        try:
            session = Session()
            user = User(**user_data)
            session.add(user)
            session.commit()
            return user.id
        except Exception as e:
            session.rollback()
            raise Exception(f"Error creating user: {str(e)}")
        finally:
            session.close()

    def _get_user_by_email(self, email):
        """
        Get a user by email.

        Args:
            email (str): The email of the user.

        Returns:
            dict: A dictionary containing user information.
        """
        try:
            session = Session()
            user = session.query(User).filter_by(email=email).first()
            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    # Add more fields as needed
                }
            else:
                return None
        except Exception as e:
            raise Exception(f"Error getting user by email: {str(e)}")
        finally:
            session.close()

    def _get_user_by_id(self, user_id):
        """
        Get a user by ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict: A dictionary containing user information.
        """
        try:
            session = Session()
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                return {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    # Add more fields as needed
                }
            else:
                return None
        except Exception as e:
            raise Exception(f"Error getting user by ID: {str(e)}")
        finally:
            session.close()
