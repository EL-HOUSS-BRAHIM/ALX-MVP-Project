import React from 'react';
import AddExpense from '../components/ExpenseTracker/AddExpense';
import ExpenseList from '../components/ExpenseTracker/ExpenseList';
import ExpenseChart from '../components/ExpenseTracker/ExpenseChart';

const ExpenseTracker = () => {
  return (
    <div>
      <h1>Expense Tracker</h1>
      <AddExpense />
      <ExpenseList />
      <ExpenseChart />
    </div>
  );
};

export default ExpenseTracker;