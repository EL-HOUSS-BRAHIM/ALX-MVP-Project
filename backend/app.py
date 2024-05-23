from flask import Flask, jsonify, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

# Load your controllers and other modules here
from controllers import AuthController, Budget_contr, Expense_contr, Reminder_contr, User_contr


# Define your API routes
@app.route('/api/v1/auth/login', methods=['POST'])
def auth_login():
    # Handle authentication requests
    return AuthController.login_user(request)

@app.route('/api/v1/auth/register', methods=['POST'])
def auth_register():
    # Handle authentication requests
    return AuthController.register_user(request)

@app.route('/api/v1/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        return User_contr.get_users()
    elif request.method == 'POST':
        return User_contr.create_user(request.json)
    elif request.method == 'PUT':
        return User_contr.update_user(request.json)
    elif request.method == 'DELETE':
        return User_contr.delete_user(request.json)

@app.route('/api/v1/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
def budgets():
    if request.method == 'GET':
        return Budget_contr.get_budgets()
    elif request.method == 'POST':
        return Budget_contr.create_budget(request.json)
    elif request.method == 'PUT':
        return Budget_contr.update_budget(request.json)
    elif request.method == 'DELETE':
        return Budget_contr.delete_budget(request.json)

# Define routes for expenses and reminders in a similar way

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
