import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getReminders, setReminder, deleteReminder } from '../services/reminder.service';

const ReminderManager = () => {
  const [reminders, setReminders] = useState([]);
  const [newReminder, setNewReminder] = useState({
    title: '',
    description: '',
    dueDate: '',
  });
  const [userId, setUserId] = useState(null); // Assuming you have a way to get the user ID

  useEffect(() => {
    const fetchReminders = async () => {
      try {
        const reminderData = await getReminders(userId);
        setReminders(reminderData);
      } catch (error) {
        console.error('Error fetching reminders:', error);
      }
    };

    if (userId) {
      fetchReminders();
    }
  }, [userId]);

  const handleCreateReminder = async (e) => {
    e.preventDefault();
    try {
      const response = await setReminder(userId, newReminder);
      if (response.error) {
        console.error('Error creating reminder:', response.error);
      } else {
        setReminders([...reminders, response.reminder]);
        setNewReminder({ title: '', description: '', dueDate: '' });
      }
    } catch (error) {
      console.error('Error creating reminder:', error);
    }
  };

  const handleDeleteReminder = async (reminderId) => {
    try {
      const response = await deleteReminder(userId, reminderId);
      if (response.error) {
        console.error('Error deleting reminder:', response.error);
      } else {
        const updatedReminders = reminders.filter((reminder) => reminder.id !== reminderId);
        setReminders(updatedReminders);
      }
    } catch (error) {
      console.error('Error deleting reminder:', error);
    }
  };

  return (
    <div>
      <h2>Reminder Manager</h2>
      <form onSubmit={handleCreateReminder}>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={newReminder.title}
          onChange={(e) => setNewReminder({ ...newReminder, title: e.target.value })}
          required
        />
        <input
          type="text"
          name="description"
          placeholder="Description"
          value={newReminder.description}
          onChange={(e) => setNewReminder({ ...newReminder, description: e.target.value })}
          required
        />
        <input
          type="date"
          name="dueDate"
          placeholder="Due Date"
          value={newReminder.dueDate}
          onChange={(e) => setNewReminder({ ...newReminder, dueDate: e.target.value })}
          required
        />
        <button type="submit">Add Reminder</button>
      </form>
      <ul>
        {reminders.map((reminder) => (
          <li key={reminder.id}>
            <h3>{reminder.title}</h3>
            <p>{reminder.description}</p>
            <p>Due Date: {reminder.dueDate}</p>
            <button onClick={() => handleDeleteReminder(reminder.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReminderManager;
