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
import mysql.connector
from database.connection import get_session

class UserDB:
    def create_user(self, user_data):
        """Create a new user in the database."""
        query = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
        values = (user_data["email"], user_data["username"], user_data["password"])
        try:
            db_connection = get_session()
            cursor = db_connection.cursor()
            cursor.execute(query, values)
            db_connection.commit()
            user_id = cursor.lastrowid
            return user_id
        except mysql.connector.Error as error:
            print(f"Error creating user: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def get_user_by_email(self, email):
        """Get a user from the database by email."""
        query = "SELECT * FROM users WHERE email = %s"
        try:
            db_connection = get_session()
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as error:
            print(f"Error retrieving user: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def update_user_profile(self, user_id, updated_data):
        """Update user profile details in the database."""
        set_clause = ", ".join([f"{key} = %s" for key in updated_data.keys()])
        values = tuple(updated_data.values())
        query = f"UPDATE users SET {set_clause} WHERE id = %s"
        values += (user_id,)
        try:
            db_connection = get_session()
            cursor = db_connection.cursor()
            cursor.execute(query, values)
            db_connection.commit()
            return cursor.rowcount
        except mysql.connector.Error as error:
            print(f"Error updating user: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()

    def delete_user(self, user_id):
        """Delete a user from the database."""
        query = "DELETE FROM users WHERE id = %s"
        try:
            db_connection = get_session()
            cursor = db_connection.cursor()
            cursor.execute(query, (user_id,))
            db_connection.commit()
            return cursor.rowcount
        except mysql.connector.Error as error:
            print(f"Error deleting user: {error}")
            raise
        finally:
            if db_connection.is_connected():
                cursor.close()
                db_connection.close()