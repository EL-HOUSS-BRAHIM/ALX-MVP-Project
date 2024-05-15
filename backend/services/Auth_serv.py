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
import bcrypt
import jwt
import datetime
from database.session import get_session
from database.models import User

class AuthService:
    def create_user(self, user_data):
        """
        Create a new user account.
        """
        session = get_session()
        email = user_data.get("email")
        username = user_data.get("username")
        password = user_data.get("password").encode("utf-8")

        # Check if user already exists
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            raise Exception("User with this email already exists")

        # Hash the password
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Create a new user
        new_user = User(email=email, username=username, password=hashed_password.decode("utf-8"))
        session.add(new_user)
        session.commit()

        return new_user

    def authenticate_user(self, credentials):
        """
        Authenticate a user and generate a JSON Web Token (JWT).
        """
        session = get_session()
        email = credentials.get("email")
        password = credentials.get("password").encode("utf-8")

        # Get the user from the database
        user = session.query(User).filter_by(email=email).first()
        if not user:
            return None

        # Check if the provided password matches the stored hash
        if bcrypt.checkpw(password, user.password.encode("utf-8")):
            # Generate a JWT
            payload = {
                "user_id": user.id,
                "email": user.email,
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
        return token

    def refreshJWT(self, token):
        """
        Refresh an existing JSON Web Token (JWT) by generating a new one.
        """
        try:
            payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
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

# Example usage
if __name__ == "__main__":
    auth_service = AuthService()
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "password123"
    }

    # Create a new user
    new_user = auth_service.create_user(user_data)
    print(f"Created user: {new_user.username}")

    # Authenticate the user
    credentials = {
        "email": "test@example.com",
        "password": "password123"
    }
    token = auth_service.authenticate_user(credentials)
    print(f"Generated token: {token}")

    # Refresh the token
    new_token = auth_service.refreshJWT(token)
    print(f"Refreshed token: {new_token}")
