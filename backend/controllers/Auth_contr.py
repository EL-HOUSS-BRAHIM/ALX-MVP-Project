#!/usr/bin/python3
import sys
sys.path.append("..")
from services.Auth_serv import AuthService
from middleware.InpuValidat import InputValidator



auth_service = AuthService()
input_validator = InputValidator()

class AuthController:
    def register_user(request):
        """
        Register a new user.
        """
        user_data = request.get_json()

        is_valid, message = input_validator.validate_user_input(user_data)
        if not is_valid:
            return {"error": message}, 400

        try:
            user = auth_service.create_user(user_data)
            return {"message": "User registered successfully"}, 201
        except Exception as e:
            return {"error": str(e)}, 500

    def login_user(request):
        """
        Authenticate and log in a user.
        """
        credentials = request.get_json()

        is_valid, message = input_validator.validate_user_input(credentials)
        if not is_valid:
            return {"error": message}, 400

        try:
            auth_token = auth_service.authenticate_user(credentials)
            if auth_token:
                return {"token": auth_token}, 200
            else:
                return {"error": "Invalid credentials"}, 401
        except Exception as e:
            return {"error": str(e)}, 500

    def logout_user(request):
        """
        Log out a user by invalidating their authentication token.
        """
        token = request.headers.get("Authorization")

        if not token:
            return {"error": "Token is required"}, 400

        try:
            auth_service.logout_user(token)
            return {"message": "Logout successful"}, 200
        except Exception as e:
            return {"error": str(e)}, 500