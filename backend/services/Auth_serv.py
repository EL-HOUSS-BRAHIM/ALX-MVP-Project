#!/usr/bin/python3
import bcrypt
import jwt
import datetime
from database.User_DataB import *
from models.User_Mod import *

user_db = UserDB()
user_model = UserModel()


class AuthService:
    def create_user(self, user_data):
        """
        Create a new user account.
        """
        email = user_data.get("email")
        username = user_data.get("username")
        password = user_data.get("password").encode("utf-8")

        # Check if user already exists
        existing_user = user_db._get_user_by_email(email)
        if existing_user:
            raise Exception("User with this email already exists")

        # Hash the password
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Create a new user
        new_user = user_model._save(email, username, hashed_password.decode("utf-8"))

        return new_user

    def authenticate_user(self, credentials):
        """
        Authenticate a user and generate a JSON Web Token (JWT).
        """
        email = credentials.get("email")
        password = credentials.get("password").encode("utf-8")

        # Get the user from the database
        user = user_db._get_user_by_email(email)
        if not user:
            return None

        # Check if the provided password matches the stored hash
        if bcrypt.checkpw(password, user["password"].encode("utf-8")):
            # Generate a JWT
            payload = {
                "user_id": user["_id"],
                "email": user["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            }
            token = self.generateJWT(payload, "secret_key")
            return token
        else:
            return None

    def generateJWT(self, payload, secret_key):
        """
        Generate a JSON Web Token (JWT) with the provided payload and secret key.
        """
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        return token.decode("utf-8")

    def refreshJWT(self, token):
        """
        Refresh an existing JSON Web Token (JWT) by generating a new one.
        """
        try:
            payload = jwt.decode(
                token.encode("utf-8"), "secret_key", algorithms=["HS256"]
            )
            user_id = payload.get("user_id")
            email = payload.get("email")

            # Generate a new JWT with updated expiration time
            new_payload = {
                "user_id": user_id,
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            }
            new_token = self.generateJWT(new_payload, "secret_key")
            return new_token
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")

    def logout_user(self, token):
        """
        Logout a user by invalidating their JWT token.
        """
        # Implement token invalidation logic
        # For example, you could store the invalidated tokens in a database or cache
        pass
