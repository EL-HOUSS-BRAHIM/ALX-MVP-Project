import React, { useState, useEffect } from 'react';
import reminderService from '../services/reminder.service';
import '../styles/reminders.css';

const ReminderList = () => {
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    const fetchReminders = async () => {
      const data = await reminderService.getReminders();
      setReminders(data);
    };
    fetchReminders();
  }, []);

  return (
    <div className="reminder-list">
      <h3>Reminders</h3>
      <ul>
        {reminders.map((reminder) => (
          <li key={reminder.id}>
            {reminder.title} - {new Date(reminder.date).toLocaleDateString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReminderList;
