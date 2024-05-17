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
from services import ExpenseService

class TestExpense(unittest.TestCase):
    def setUp(self):
        self.service = ExpenseService()
        self.user_id = "user1"
        self.expense_data = {
            "category": "Food",
            "amount": 50.0,
            "description": "Groceries",
        }

    def test_add_expense(self):
        result = self.service.add_expense(self.user_id, self.expense_data)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Expense added successfully")
        self.assertIn("expense_id", result)

    def test_get_expenses(self):
        # Add an expense first
        self.service.add_expense(self.user_id, self.expense_data)

        result = self.service.get_expenses(self.user_id)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_update_expense(self):
        # Add an expense first
        expense_result = self.service.add_expense(self.user_id, self.expense_data)
        expense_id = expense_result["expense_id"]

        updated_data = {
            "category": "Entertainment",
            "amount": 100.0,
        }
        result = self.service.update_expense(self.user_id, expense_id, updated_data)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Expense updated successfully")

    def test_delete_expense(self):
        # Add an expense first
        expense_result = self.service.add_expense(self.user_id, self.expense_data)
        expense_id = expense_result["expense_id"]

        result = self.service.delete_expense(self.user_id, expense_id)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Expense deleted successfully")

if __name__ == "__main__":
    unittest.main()