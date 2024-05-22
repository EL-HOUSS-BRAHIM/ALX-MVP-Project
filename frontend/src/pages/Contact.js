import React from 'react';

const Content = () => {
  return (
    <main className="content">
      <div id="home" className="active">
        <h2>Welcome to Your Dashboard</h2>
        <p>This is your personal finance management dashboard.</p>
      </div>
      <div id="budget" className="hidden">
        <h2>Budget Manager</h2>
        {/* Add your Budget Manager content here */}
      </div>
      <div id="expenses" className="hidden">
        <h2>Expense Tracker</h2>
        {/* Add your Expense Tracker content here */}
      </div>
      <div id="reminders" className="hidden">
        <h2>Reminder Manager</h2>
        {/* Add your Reminder Manager content here */}
      </div>
      <div id="profile" className="hidden">
        <h2>User Profile</h2>
        {/* Add your User Profile content here */}
      </div>
    </main>
  );
};

export default Content;