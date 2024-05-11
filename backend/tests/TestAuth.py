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
import unittest
from services.Auth_serv import AuthService
from unittest.mock import patch, MagicMock
from middleware.InpuValidat import InputValidator


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.input_validator = InputValidator()

    @patch("services.AuthService.AuthService.create_user")
    def test_register_user(self, mock_create_user):
        user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123",
        }

        mock_create_user.return_value = {"_id": "1234"}

        is_valid, message = self.input_validator.validate_user_input(user_data)
        self.assertTrue(is_valid)

        user = self.auth_service.create_user(user_data)
        self.assertIsNotNone(user)
        self.assertEqual(user["_id"], "1234")

    @patch("services.AuthService.AuthService.authenticate_user")
    def test_login_user(self, mock_authenticate_user):
        credentials = {"email": "test@example.com", "password": "password123"}

        mock_authenticate_user.return_value = "mock_token"

        is_valid, message = self.input_validator.validate_user_input(credentials)
        self.assertTrue(is_valid)

        token = self.auth_service.authenticate_user(credentials)
        self.assertEqual(token, "mock_token")

    @patch("services.AuthService.AuthService.logout_user")
    def test_logout_user(self, mock_logout_user):
        token = "mock_token"
        mock_logout_user.return_value = None

        self.auth_service.logout_user(token)
        mock_logout_user.assert_called_once_with(token)

    @patch("services.AuthService.AuthService.authenticate_user")
    def test_authenticate_user(self, mock_authenticate_user):
        credentials = {"email": "test@example.com", "password": "password123"}

        mock_authenticate_user.return_value = "mock_token"

        token = self.auth_service.authenticate_user(credentials)
        self.assertEqual(token, "mock_token")

    @patch("services.AuthService.AuthService.generateJWT")
    def test_generate_jwt(self, mock_generate_jwt):
        payload = {"user_id": "1234", "email": "test@example.com"}
        mock_generate_jwt.return_value = "mock_token"

        token = self.auth_service.generateJWT(payload, "secret_key")
        self.assertEqual(token, "mock_token")

    @patch("services.AuthService.AuthService.refreshJWT")
    def test_refresh_jwt(self, mock_refresh_jwt):
        token = "mock_token"
        mock_refresh_jwt.return_value = "new_mock_token"

        new_token = self.auth_service.refreshJWT(token)
        self.assertEqual(new_token, "new_mock_token")


if __name__ == "__main__":
    unittest.main()
