import unittest
from services import ReminderService

class TestReminder(unittest.TestCase):
    def setUp(self):
        self.service = ReminderService()
        self.user_id = "user1"
        self.reminder_data = {
            "title": "Buy groceries",
            "description": "Don't forget to buy milk and eggs",
            "due_date": "2023-05-15",
        }

    def test_set_reminder(self):
        result = self.service.set_reminder(self.user_id, self.reminder_data)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Reminder set successfully")
        self.assertIn("reminder_id", result)

    def test_get_reminders(self):
        # Set a reminder first
        self.service.set_reminder(self.user_id, self.reminder_data)

        result = self.service.get_reminders(self.user_id)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_delete_reminder(self):
        # Set a reminder first
        reminder_result = self.service.set_reminder(self.user_id, self.reminder_data)
        reminder_id = reminder_result["reminder_id"]

        result = self.service.delete_reminder(self.user_id, reminder_id)
        self.assertIn("message", result)
        self.assertEqual(result["message"], "Reminder deleted successfully")

if __name__ == "__main__":
    unittest.main()