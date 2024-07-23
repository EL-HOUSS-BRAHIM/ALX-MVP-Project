import React from 'react';
import AddReminder from '../components/AddReminder';
import ReminderList from '../components/ReminderList';
import '../styles/reminders.css';

const ReminderManager = () => {
  return (
    <div className="reminder-manager">
      <AddReminder />
      <ReminderList />
    </div>
  );
};

export default ReminderManager;
