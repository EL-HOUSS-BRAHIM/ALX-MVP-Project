import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faUser, faChartPie, faDollarSign, faBell } from '@fortawesome/free-solid-svg-icons';
import '../styles/header.css';

const Header = () => {
  return (
    <header className="header">
      <h1>Budget Tracker</h1>
      <nav>
        <Link to="/"><FontAwesomeIcon icon={faHome} /> Home</Link>
        <Link to="/budget"><FontAwesomeIcon icon={faDollarSign} /> Budget</Link>
        <Link to="/expenses"><FontAwesomeIcon icon={faChartPie} /> Expenses</Link>
        <Link to="/reminders"><FontAwesomeIcon icon={faBell} /> Reminders</Link>
        <Link to="/profile"><FontAwesomeIcon icon={faUser} /> Profile</Link>
      </nav>
    </header>
  );
};

export default Header;

