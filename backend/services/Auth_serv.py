#!/usr/bin/python3
from models.User_Mod import UserModel
import datetime
import jwt
import bcrypt
import sys
import os

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Convert sys.path to a set to remove duplicates, then convert it back to a list
unique_sys_path = list(set(sys.path))

# Print the unique entries in sys.path
for path in unique_sys_path:
    print(path)

# Constants
JWT_SECRET_KEY = "your_secret_key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME = 3600  # 1 hour


class AuthService:
    def create_user(self, user_data):
        """
        Create a new user account.

        Args:
            user_data (dict): A dictionary containing user information (e.g., email, password, name).

        Returns:
            dict: A dictionary containing the user's information and a success message.
        """
        try:
            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(
                user_data["password"].encode("utf-8"), bcrypt.gensalt()
            )
            user_data["password"] = hashed_password.decode("utf-8")

            # Save the user data to the database
            user_model = UserModel()
            user_id = user_model._save(user_data)

            return {
                "success": True,
                "message": "User created successfully.",
                "user_id": user_id,
            }
        except Exception as e:
            return {"success": False, "message": f"Error creating user: {str(e)}"}

    def authenticate_user(email, password):
        """
        Authenticate a user by email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            dict: A dictionary containing the authentication result and a JWT token (if successful).
        """
        try:
            # Retrieve the user from the database
            user_model = UserModel()
            user = user_model._get_by_email(email)

            if user:
                # Check if the provided password matches the hashed password
                if bcrypt.checkpw(
                    password.encode("utf-8"), user["password"].encode("utf-8")
                ):
                    # Generate a JWT token
                    payload = {
                        "email": email,
                        "exp": datetime.datetime.utcnow()
                        + datetime.timedelta(seconds=JWT_EXPIRATION_TIME),
                    }
                    token = jwt.encode(payload, JWT_SECRET_KEY,
                                       algorithm=JWT_ALGORITHM)

                    return {"success": True, "token": token}
                else:
                    return {"success": False, "message": "Invalid email or password."}
            else:
                return {"success": False, "message": "User not found."}
        except Exception as e:
            return {"success": False, "message": f"Error authenticating user: {str(e)}"}

    def generate_jwt(payload, expires_in=JWT_EXPIRATION_TIME):
        """
        Generate a JSON Web Token (JWT).

        Args:
            payload (dict): The payload to be encoded in the JWT.
            expires_in (int, optional): The expiration time of the JWT in seconds. Default is JWT_EXPIRATION_TIME.

        Returns:
            str: The generated JWT token.
        """
        try:
            payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(
                seconds=expires_in
            )
            token = jwt.encode(payload, JWT_SECRET_KEY,
                               algorithm=JWT_ALGORITHM)
            return token
        except Exception as e:
            raise Exception(f"Error generating JWT: {str(e)}")

    def refresh_jwt(token):
        """
        Refresh a JSON Web Token (JWT).

        Args:
            token (str): The JWT token to be refreshed.


        Returns:
            dict: A dictionary containing the refresh result and a new JWT token (if successful).
        """
        try:
            # Decode the JWT token
            payload = jwt.decode(token, JWT_SECRET_KEY,
                                 algorithms=[JWT_ALGORITHM])

            # Generate a new JWT token with a new expiration time
            new_token = generate_jwt(payload)

            return {"success": True, "token": new_token}
        except jwt.ExpiredSignatureError:
            return {"success": False, "message": "JWT token has expired."}
        except jwt.InvalidTokenError:
            return {"success": False, "message": "Invalid JWT token."}
        except Exception as e:
            return {"success": False, "message": f"Error refreshing JWT: {str(e)}"}

    def logout_user(token):
        """
        Invalidate a user's JWT token.

        Args:
            token (str): The JWT token to be invalidated.

        Returns:
            dict: A dictionary containing the logout result and a success message.
        """

        try:
        # Decode the JWT token
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])

        # Invalidate the token (e.g., store it in a blacklist or clear user session)
        # ...

            return {"success": True, "message": "User logged out successfully."}
        except jwt.ExpiredSignatureError:
            return {"success": False, "message": "JWT token has expired."}
        except jwt.InvalidTokenError:
            return {"success": False, "message": "Invalid JWT token."}
        except Exception as e:
            return {"success": False, "message": f"Error logging out user: {str(e)}"}
