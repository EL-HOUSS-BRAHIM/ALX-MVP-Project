import React, { useState } from 'react';
import ExpenseTracker from './ExpenseTracker';

const ExpenseTrackerDemo = () => {
  const [expenseData, setExpenseData] = useState({
    expenses: [
      { id: 1, category: 'Groceries', description: 'Weekly grocery shopping', amount: 120, date: '2023-05-01' },
      { id: 2, category: 'Transportation', description: 'Gas for car', amount: 50, date: '2023-05-03' },
      { id: 3, category: 'Entertainment', description: 'Movie tickets', amount: 30, date: '2023-05-07' },
      { id: 4, category: 'Utilities', description: 'Electricity bill', amount: 80, date: '2023-05-10' },
    ],
  });

  const handleExpenseUpdate = (newExpenseData) => {
    setExpenseData(newExpenseData);
  };

  return (
    <div className="demo-section">
      <h2>Expense Tracker</h2>
      <ExpenseTracker expenseData={expenseData} onExpenseUpdate={handleExpenseUpdate} />
    </div>
  );
};

export default ExpenseTrackerDemo;