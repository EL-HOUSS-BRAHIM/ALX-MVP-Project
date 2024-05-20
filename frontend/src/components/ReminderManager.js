import React, { useState, useEffect } from 'react';
import { deleteReminder, getReminders, setReminder } from '../services/reminder.service';

const ReminderManager = () => {
  const [reminders, setReminders] = useState([]);
  const [newReminder, setNewReminder] = useState({
    title: '',
    description: '',
    dueDate: '',
  });

  useEffect(() => {
    const fetchReminders = async () => {
      try {
        const reminderData = await getReminders();
        setReminders(reminderData);
      } catch (error) {
        console.error('Error fetching reminders:', error);
      }
    };

    fetchReminders();
  }, []);

  const handleCreateReminder = async (e) => {
    e.preventDefault();
    try {
      await setReminder(newReminder);
      setNewReminder({ title: '', description: '', dueDate: '' });
      // Handle successful reminder creation
    } catch (error) {
      console.error('Error creating reminder:', error);
      // Handle error
    }
  };

  const handleDeleteReminder = async (reminderId) => {
    try {
      await deleteReminder(reminderId);
      const updatedReminders = reminders.filter((reminder) => reminder.id !== reminderId);
      setReminders(updatedReminders);
      // Handle successful reminder deletion
    } catch (error) {
      console.error('Error deleting reminder:', error);
      // Handle error
    }
  };

  const handleUpdateReminder = async (updatedReminder) => {
    try {
      await setReminder(updatedReminder);
      const updatedReminders = reminders.map((reminder) =>
        reminder.id === updatedReminder.id ? updatedReminder : reminder
      );
      setReminders(updatedReminders);
      // Handle successful reminder update
    } catch (error) {
      console.error('Error updating reminder:', error);
      // Handle error
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
            <button onClick={() => handleUpdateReminder({ ...reminder, description: `${reminder.description} (Updated)` })}>
              Update
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReminderManager;