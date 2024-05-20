import React, { useState, useEffect } from 'react';
import { deleteBudget, getBudgetSummary, setBudget, updateBudget } from '../services/budget.service';

const BudgetManager = () => {
  const [budgets, setBudgets] = useState([]);
  const [newBudget, setNewBudget] = useState({
    name: '',
    amount: 0,
  });

  useEffect(() => {
    const fetchBudgets = async () => {
      try {
        const budgetSummary = await getBudgetSummary();
        setBudgets(budgetSummary);
      } catch (error) {
        console.error('Error fetching budgets:', error);
      }
    };

    fetchBudgets();
  }, []);

  const handleCreateBudget = async (e) => {
    e.preventDefault();
    try {
      await setBudget(newBudget);
      setNewBudget({ name: '', amount: 0 });
      // Handle successful budget creation
    } catch (error) {
      console.error('Error creating budget:', error);
      // Handle error
    }
  };

  const handleDeleteBudget = async (budgetId) => {
    try {
      await deleteBudget(budgetId);
      const updatedBudgets = budgets.filter((budget) => budget.id !== budgetId);
      setBudgets(updatedBudgets);
      // Handle successful budget deletion
    } catch (error) {
      console.error('Error deleting budget:', error);
      // Handle error
    }
  };

  const handleUpdateBudget = async (updatedBudget) => {
    try {
      await updateBudget(updatedBudget);
      const updatedBudgets = budgets.map((budget) =>
        budget.id === updatedBudget.id ? updatedBudget : budget
      );
      setBudgets(updatedBudgets);
      // Handle successful budget update
    } catch (error) {
      console.error('Error updating budget:', error);
      // Handle error
    }
  };

  return (
    <div>
      <h2>Budget Manager</h2>
      <form onSubmit={handleCreateBudget}>
        <input
          type="text"
          name="name"
          placeholder="Budget Name"
          value={newBudget.name}
          onChange={(e) => setNewBudget({ ...newBudget, name: e.target.value })}
          required
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={newBudget.amount}
          onChange={(e) => setNewBudget({ ...newBudget, amount: parseFloat(e.target.value) })}
          required
        />
        <button type="submit">Create Budget</button>
      </form>
      <ul>
        {budgets.map((budget) => (
          <li key={budget.id}>
            {budget.name} - {budget.amount}
            <button onClick={() => handleDeleteBudget(budget.id)}>Delete</button>
            <button onClick={() => handleUpdateBudget({ ...budget, amount: budget.amount + 100 })}>
              Increase
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BudgetManager;