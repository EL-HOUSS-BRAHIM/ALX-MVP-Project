import React, { useState, useEffect } from 'react';
import budgetService from '../services/budget.service';
import '../styles/budget.css';

const BudgetSummary = () => {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    const fetchSummary = async () => {
      const data = await budgetService.getBudgetSummary();
      setSummary(data);
    };
    fetchSummary();
  }, []);

  return (
    <div className="budget-summary">
      {summary ? (
        <>
          <h3>Budget Summary</h3>
          <p>Monthly Budget: ${summary.budget}</p>
          <p>Total Expenses: ${summary.expenses}</p>
          <p>Remaining Budget: ${summary.remaining}</p>
        </>
      ) : (
        <p>Loading summary...</p>
      )}
    </div>
  );
};

export default BudgetSummary;
