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
from flask import Flask
from database.connection import get_session
from controllers import AuthController, UserController, ExpenseController, BudgetController, ReminderController

app = Flask(__name__)

# Register controllers
AuthController.register_routes(app)
UserController.register_routes(app)
ExpenseController.register_routes(app)
BudgetController.register_routes(app)
ReminderController.register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
