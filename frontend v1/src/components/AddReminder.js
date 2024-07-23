import React, { useState } from 'react';
import reminderService from '../services/reminder.service';
import '../styles/reminders.css';

const AddReminder = () => {
  const [reminder, setReminder] = useState({ title: '', date: '' });

  const handleChange = (e) => {
    setReminder({ ...reminder, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await reminderService.addReminder(reminder);
      // Optionally reset form and/or show success message
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="add-reminder">
      <h3>Add Reminder</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={reminder.title}
          onChange={handleChange}
          required
        />
        <input
          type="date"
          name="date"
          value={reminder.date}
          onChange={handleChange}
          required
        />
        <button type="submit">Add Reminder</button>
      </form>
    </div>
  );
};

export default AddReminder;
