#!/usr/bin/python3
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
