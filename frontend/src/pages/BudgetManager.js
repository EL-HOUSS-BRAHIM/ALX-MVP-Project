import React from 'react';
import SetBudget from '../components/BudgetManager/SetBudget';
import BudgetSummary from '../components/BudgetManager/BudgetSummary';
import BudgetChart from '../components/BudgetManager/BudgetChart';

const BudgetManager = () => {
  return (
    <div>
      <h1>Budget Manager</h1>
      <SetBudget />
      <BudgetSummary />
      <BudgetChart />
    </div>
  );
};

export default BudgetManager;