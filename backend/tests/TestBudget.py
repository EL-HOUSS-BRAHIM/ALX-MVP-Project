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
from services.Budget_serv import BudgetService

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService()
        self.user_id = "user1"
        self.budget_data = {
            "amount": 1000.0,
            "category": "Food",
            "start_date": "2023-05-01",
            "end_date": "2023-05-31",
        }

    def test_set_budget(self):
        result = self.service.set_budget(self.user_id, self.budget_data)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Budget set successfully")

    def test_get_budget_summary(self):
        # Set a budget first
        self.service.set_budget(self.user_id, self.budget_data)

        result = self.service.get_budget_summary(self.user_id)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["amount"], self.budget_data["amount"])
        self.assertEqual(result["category"], self.budget_data["category"])
        self.assertEqual(result["start_date"], self.budget_data["start_date"])
        self.assertEqual(result["end_date"], self.budget_data["end_date"])

    def test_update_budget(self):
        # Set a budget first
        self.service.set_budget(self.user_id, self.budget_data)

        updated_data = {
            "amount": 1500.0,
            "category": "Entertainment",
        }
        result = self.service.update_budget(self.user_id, updated_data)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Budget updated successfully")

    def test_delete_budget(self):
        # Set a budget first
        self.service.set_budget(self.user_id, self.budget_data)

        result = self.service.delete_budget(self.user_id)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Budget deleted successfully")

if __name__ == "__main__":
    unittest.main()