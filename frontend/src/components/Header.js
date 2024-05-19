import React from 'react';
import { Link } from 'react-router-dom';
import { isAuthenticated, logout } from '../services/auth.service';

const Header = () => {
  const handleLogout = () => {
    logout();
    // Redirect to the login page or the homepage after logout
  };

  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/budget">Budget Manager</Link>
          </li>
          <li>
            <Link to="/expenses">Expense Tracker</Link>
          </li>
          <li>
            <Link to="/reminders">Reminder Manager</Link>
          </li>
          {isAuthenticated() ? (
            <>
              <li>
                <Link to="/profile">Profile</Link>
              </li>
              <li>
                <button onClick={handleLogout}>Logout</button>
              </li>
            </>
          ) : (
            <>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/register">Register</Link>
              </li>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
