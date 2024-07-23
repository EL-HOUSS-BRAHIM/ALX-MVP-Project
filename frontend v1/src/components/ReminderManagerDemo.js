import React, { useState } from 'react';
import ReminderManager from './ReminderManager';

const ReminderManagerDemo = () => {
  const [reminderData, setReminderData] = useState({
    reminders: [
      { id: 1, title: 'Pay rent', dueDate: '2023-06-01', recurring: true },
      { id: 2, title: 'Car insurance payment', dueDate: '2023-06-15', recurring: false },
      { id: 3, title: 'Dentist appointment', dueDate: '2023-06-20', recurring: false },
      { id: 4, title: 'Birthday party', dueDate: '2023-07-05', recurring: true },
    ],
  });

  const handleReminderUpdate = (newReminderData) => {
    setReminderData(newReminderData);
  };

  return (
    <div className="demo-section">
      <h2>Reminder Manager</h2>
      <ReminderManager reminderData={reminderData} onReminderUpdate={handleReminderUpdate} />
    </div>
  );
};

export default ReminderManagerDemo;