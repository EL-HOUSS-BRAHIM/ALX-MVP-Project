import React, { useState } from 'react';
import budgetService from '../services/budget.service';
import '../styles/budget.css';

const SetBudget = () => {
  const [budget, setBudget] = useState('');

  const handleChange = (e) => {
    setBudget(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await budgetService.setBudget(budget);
      // Optionally reset form and/or show success message
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="set-budget">
      <h3>Set Budget</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="budget"
          placeholder="Monthly Budget"
          value={budget}
          onChange={handleChange}
          required
        />
        <button type="submit">Set Budget</button>
      </form>
    </div>
  );
};

export default SetBudget;
