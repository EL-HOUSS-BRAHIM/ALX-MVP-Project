import React from 'react';
import SetBudget from '../components/SetBudget';
import BudgetSummary from '../components/BudgetSummary';
import BudgetChart from '../components/BudgetChart';
import '../styles/budget.css';

const BudgetManager = () => {
  return (
    <div className="budget-manager">
      <SetBudget />
      <BudgetSummary />
      <BudgetChart />
    </div>
  );
};

export default BudgetManager;
