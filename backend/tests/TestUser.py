#!/usr/bin/python3
import unittest
from unittest.mock import patch, MagicMock
from services.User_serv import UserService
from middleware.InpuValidat import InputValidator

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()
        self.input_validator = InputValidator()

    @patch('services.UserService.UserService.get_user_profile')
    def test_get_user_profile(self, mock_get_user_profile):
        user_id = '1234'
        mock_user_profile = {
            '_id': '1234',
            'email': 'test@example.com',
            'username': 'testuser'
        }
        mock_get_user_profile.return_value = mock_user_profile

        user_profile = self.user_service.get_user_profile(user_id)
        self.assertEqual(user_profile, mock_user_profile)

    @patch('services.UserService.UserService.update_user_profile')
    def test_update_user_profile(self, mock_update_user_profile):
        user_id = '1234'
        updated_data = {
            'username': 'newusername',
            'email': 'newemail@example.com'
        }
        mock_update_user_profile.return_value = True

        is_valid, message = self.input_validator.validate_user_input(updated_data)
        self.assertTrue(is_valid)

        result = self.user_service.update_user_profile(user_id, updated_data)
        self.assertTrue(result)

    @patch('services.UserService.UserService.delete_user')
    def test_delete_user(self, mock_delete_user):
        user_id = '1234'
        mock_delete_user.return_value = True

        result = self.user_service.delete_user(user_id)
        self.assertTrue(result)

    @patch('services.UserService.UserService.trackLoginAttempts')
    def test_track_login_attempts(self, mock_track_login_attempts):
        user_id = '1234'
        mock_track_login_attempts.return_value = True

        result = self.user_service.trackLoginAttempts(user_id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
