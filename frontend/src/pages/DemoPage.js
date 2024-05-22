import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import BudgetManagerDemo from '../components/BudgetManagerDemo';
import ExpenseTrackerDemo from '../components/ExpenseTrackerDemo';
import ReminderManagerDemo from '../components/ReminderManagerDemo';
import '../styles/demo.css';

const DemoPage = () => {
  return (
    <div className="demo-page">
      <Header />
      <div className="demo-container">
        <h1>Live Demo</h1>
        <BudgetManagerDemo />
        <ExpenseTrackerDemo />
        <ReminderManagerDemo />
      </div>
      <Footer />
    </div>
  );
};

export default DemoPage;