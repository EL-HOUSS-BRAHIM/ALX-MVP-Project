import React from 'react';
import AddExpense from '../components/AddExpense';
import ExpenseList from '../components/ExpenseList';
import ExpenseChart from '../components/ExpenseChart';
import '../styles/expenses.css';

const ExpenseTracker = () => {
  return (
    <div className="expense-tracker">
      <AddExpense />
      <ExpenseList />
      <ExpenseChart />
    </div>
  );
};

export default ExpenseTracker;
