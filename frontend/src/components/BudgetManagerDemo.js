import React, { useState } from 'react';
import BudgetManager from './BudgetManager';

const BudgetManagerDemo = () => {
  const [budgetData, setBudgetData] = useState({
    totalBudget: 5000,
    categories: [
      { name: 'Rent', amount: 1500 },
      { name: 'Groceries', amount: 800 },
      { name: 'Utilities', amount: 300 },
      { name: 'Transportation', amount: 200 },
      { name: 'Entertainment', amount: 500 },
    ],
  });

  const handleBudgetUpdate = (newBudgetData) => {
    setBudgetData(newBudgetData);
  };

  return (
    <div className="demo-section">
      <h2>Budget Manager</h2>
      <BudgetManager budgetData={budgetData} onBudgetUpdate={handleBudgetUpdate} />
    </div>
  );
};

export default BudgetManagerDemo;