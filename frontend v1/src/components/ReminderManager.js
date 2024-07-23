// components/ReminderManager.js
import React, { useState, useEffect } from 'react';
import api from '../utils/api';

const ReminderManager = () => {
  const [reminders, setReminders] = useState([]);
  const [newReminder, setNewReminder] = useState({ title: '', description: '', dueDate: '' });

  useEffect(() => {
    fetchReminders();
  }, []);

  const fetchReminders = async () => {
    try {
      const response = await api.get('/reminders');
      setReminders(response.data);
    } catch (error) {
      console.error('Error fetching reminders:', error);
    }
  };

  const handleInputChange = (e) => {
    setNewReminder({ ...newReminder, [e.target.name]: e.target.value });
  };

  const handleCreateReminder = async () => {
    try {
      await api.post('/reminders', newReminder);
      setNewReminder({ title: '', description: '', dueDate: '' });
      fetchReminders();
    } catch (error) {
      console.error('Error creating reminder:', error);
    }
  };

  const handleDeleteReminder = async (reminderId) => {
    try {
      await api.delete(`/reminders/${reminderId}`);
      fetchReminders();
    } catch (error) {
      console.error('Error deleting reminder:', error);
    }
  };

  return (
    <div>
      <div>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={newReminder.title}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="description"
          placeholder="Description"
          value={newReminder.description}
          onChange={handleInputChange}
        />
        <input
          type="date"
          name="dueDate"
          placeholder="Due Date"
          value={newReminder.dueDate}
          onChange={handleInputChange}
        />
        <button onClick={handleCreateReminder}>Add Reminder</button>
      </div>
      <ul>
        {reminders.map((reminder) => (
          <li key={reminder.id}>
            <span>{reminder.title}</span>
            <span>{reminder.description}</span>
            <span>{reminder.dueDate}</span>
            <button onClick={() => handleDeleteReminder(reminder.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReminderManager;