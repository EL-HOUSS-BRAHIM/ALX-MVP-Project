import React from 'react';
import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <div>
      <h1>Welcome to Our App</h1>
      <p>Manage your finances, track expenses, and set reminders with ease.</p>
      <Link to="/register">Get Started</Link>
      {/* You can add more content or styling as needed */}
    </div>
  );
};

export default LandingPage;
