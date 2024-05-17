from database.connection import get_session
from database.models import Expense, User
from middleware import InputValidator

class ExpenseService:
    def __init__(self):
        self.validator = InputValidator()

    def add_expense(self, user_id, expense_data):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        if not self.validator.validate_expense_data(expense_data):
            return {"error": "Invalid expense data"}

        expense = Expense(
            user=user,
            category=expense_data["category"],
            amount=expense_data["amount"],
            description=expense_data.get("description"),
        )
        session.add(expense)
        session.commit()

        return {"message": "Expense added successfully", "expense_id": expense.id}

    def get_expenses(self, user_id):
        session = get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return {"error": "Invalid user ID"}

        expenses = user.expenses
        return [expense.to_dict() for expense in expenses]

    def update_expense(self, user_id, expense_id, updated_data):
        session = get_session()
        expense = session.query(Expense).filter_by(id=expense_id, user_id=user_id).first()
        if not expense:
            return {"error": "Expense not found"}

        if not self.validator.validate_expense_data(updated_data):
            return {"error": "Invalid expense data"}

        expense.category = updated_data["category"]
        expense.amount = updated_data["amount"]
        expense.description = updated_data.get("description")
        session.commit()

        return {"message": "Expense updated successfully"}

    def delete_expense(self, user_id, expense_id):
        session = get_session()
        expense = session.query(Expense).filter_by(id=expense_id, user_id=user_id).first()
        if not expense:
            return {"error": "Expense not found"}

        session.delete(expense)
        session.commit()

        return {"message": "Expense deleted successfully"}