from services import User


class UserController:
    def __init__(self):
        self.service = User()

    def get_user_profile(self, request):
        """
        Get the user profile details.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: The user profile details or an error message.
        """
        user_id = request.get("user_id")
        return self.service.get_user_profile(user_id)

    def update_user_profile(self, request):
        """
        Update the user profile details.

        Args:
            request (dict): The request data containing the user ID and updated profile data.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        profile_data = request.get("profile_data")
        return self.service.update_user_profile(user_id, profile_data)

    def delete_user(self, request):
        """
        Delete a user account.

        Args:
            request (dict): The request data containing the user ID.

        Returns:
            dict: A success or error message.
        """
        user_id = request.get("user_id")
        return self.service.delete_user(user_id)
