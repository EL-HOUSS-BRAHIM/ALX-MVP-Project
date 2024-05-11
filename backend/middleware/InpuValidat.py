#!/usr/bin/python3
import re
from datetime import datetime
from utils.JWT import checkJWTExpiration


class InputValidator:
    def validate_user_input(self, user_data):
        """
        Validate user input data such as username, email, password, etc.
        based on defined rules (e.g., email format, password strength, etc.).
        """
        username = user_data.get("username")
        email = user_data.get("email")
        password = user_data.get("password")

        if not username or not email or not password:
            return False, "All fields (username, email, password) are required."

        if len(username) < 4:
            return False, "Username must be at least 4 characters long."

        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return False, "Invalid email format."

        if len(password) < 8:
            return False, "Password must be at least 8 characters long."

        return True, "Valid user input."

    def validate_expense_input(self, expense_data):
        """
        Validate expense input data such as amount, category, date, etc.
        based on defined rules (e.g., amount should be a number, date format, etc.).
        """
        amount = expense_data.get("amount")
        category = expense_data.get("category")
        date = expense_data.get("date")

        if not amount or not category or not date:
            return False, "All fields (amount, category, date) are required."

        try:
            amount = float(amount)
        except ValueError:
            return False, "Amount must be a valid number."

        if amount <= 0:
            return False, "Amount must be greater than zero."

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Expected format: YYYY-MM-DD."

        return True, "Valid expense input."

    def validate_budget_input(self, budget_data):
        """
        Validate budget input data such as amount, category, period, etc.
        based on defined rules (e.g., amount should be a number, valid date range, etc.).
        """
        amount = budget_data.get("amount")
        category = budget_data.get("category")
        start_date = budget_data.get("start_date")
        end_date = budget_data.get("end_date")

        if not amount or not category or not start_date or not end_date:
            return (
                False,
                "All fields (amount, category, start_date, end_date) are required.",
            )

        try:
            amount = float(amount)
        except ValueError:
            return False, "Amount must be a valid number."

        if amount <= 0:
            return False, "Amount must be greater than zero."

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Expected format: YYYY-MM-DD."

        if start_date >= end_date:
            return False, "Start date must be before end date."

        return True, "Valid budget input."

    def validate_reminder_input(self, reminder_data):
        """
        Validate reminder input data such as title, description, due date, etc.
        based on defined rules (e.g., date format, non-empty fields, etc.).
        """
        title = reminder_data.get("title")
        description = reminder_data.get("description")
        due_date = reminder_data.get("due_date")

        if not title or not description or not due_date:
            return False, "All fields (title, description, due_date) are required."

        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            return False, "Invalid date format. Expected format: YYYY-MM-DD."

        return True, "Valid reminder input."

    def validateJWT(self, token):
        """
        Validate the JSON Web Token (JWT) for authentication purposes.
        """
        if not token:
            return False, "Token is required."

        if not checkJWTExpiration(token):
            return False, "Token has expired."

        # Additional JWT validation logic can be added here

        return True, "Valid token."

    def implementRateLimiting(self, userId):
        """
        Implement rate limiting mechanism to prevent abuse or excessive requests.
        """
        # Implement rate limiting logic based on userId
        # This could involve storing request counts in a database or cache
        # and limiting requests based on a predefined threshold
        pass
