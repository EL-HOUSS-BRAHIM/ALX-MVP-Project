import React from 'react';
import AddReminder from '../components/ReminderManager/AddReminder';
import ReminderList from '../components/ReminderManager/ReminderList';

const ReminderManager = () => {
  return (
    <div>
      <h1>Reminder Manager</h1>
      <AddReminder />
      <ReminderList />
    </div>
  );
};

export default ReminderManager;