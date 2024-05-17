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
import re
from datetime import datetime
from utils.JWT import checkJWTExpiration

class Promise:
    def __init__(self, executor):
        self.callbacks = []
        self.errbacks = []
        self.value = None
        self.error = None

        def resolve(value):
            self.value = value
            for callback in self.callbacks:
                callback(value)

        def reject(error):
            self.error = error
            for errback in self.errbacks:
                errback(error)

        executor(resolve, reject)

    def then(self, callback):
        if self.value:
            callback(self.value)
        else:
            self.callbacks.append(callback)
        return self

    def catch(self, errback):
        if self.error:
            errback(self.error)
        else:
            self.errbacks.append(errback)
        return self

    @staticmethod
    def resolve(value):
        return Promise(lambda resolve, _: resolve(value))

    @staticmethod
    def reject(error):
        return Promise(lambda _, reject: reject(error))
class InputValidator:
    def validate_user_input(self, credentials):
        if 'email' not in credentials or 'password' not in credentials:
            return False, "Missing email or password"
        if not isinstance(credentials['email'], str) or not isinstance(credentials['password'], str):
            return False, "Email and password must be strings"
        if '@' not in credentials['email']:
            return False, "Invalid email format"
        if len(credentials['password']) < 8:
            return False, "Password must be at least 8 characters"
        return True, "Valid input"

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
