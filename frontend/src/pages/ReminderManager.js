import React, { useEffect, useState } from "react";
import {
  getReminders,
  createReminder,
  updateReminder,
  deleteReminder,
} from "../services/reminder.service";

const ReminderManager = () => {
  const [reminders, setReminders] = useState([]);
  const [newReminderTitle, setNewReminderTitle] = useState("");
  const [newReminderDate, setNewReminderDate] = useState("");

  useEffect(() => {
    fetchReminders();
  }, []);

  const fetchReminders = async () => {
    try {
      const remindersData = await getReminders();
      setReminders(remindersData);
    } catch (error) {
      console.error("Error fetching reminders:", error);
    }
  };

  const handleCreateReminder = async () => {
    try {
      await createReminder(newReminderTitle, newReminderDate);
      setNewReminderTitle("");
      setNewReminderDate("");
      fetchReminders();
    } catch (error) {
      console.error("Error creating reminder:", error);
    }
  };

  const handleUpdateReminder = async (reminderId, updates) => {
    try {
      await updateReminder(reminderId, updates);
      fetchReminders();
    } catch (error) {
      console.error("Error updating reminder:", error);
    }
  };

  const handleDeleteReminder = async (reminderId) => {
    try {
      await deleteReminder(reminderId);
      fetchReminders();
    } catch (error) {
      console.error("Error deleting reminder:", error);
    }
  };

  return (
    <div>
      <ul>
        {reminders.map((reminder) => (
          <li key={reminder.id}>
            <h3>{reminder.title}</h3>
            <p>Date: {reminder.date}</p>
            <button onClick={() => handleUpdateReminder(reminder.id, { date: "2023-06-15" })}>
              Update Date
            </button>
            <button onClick={() => handleDeleteReminder(reminder.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <h3>Create New Reminder</h3>
      <input
        type="text"
        placeholder="Reminder Title"
        value={newReminderTitle}
        onChange={(e) => setNewReminderTitle(e.target.value)}
      />
      <input
        type="date"
        value={newReminderDate}
        onChange={(e) => setNewReminderDate(e.target.value)}
      />
      <button onClick={handleCreateReminder}>Create Reminder</button>
    </div>
  );
};

export default ReminderManager;