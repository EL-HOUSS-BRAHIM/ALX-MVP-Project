// components/BudgetManager.js
import React, { useState, useEffect } from 'react';
import api from '../utils/api';

const BudgetManager = () => {
  const [budgets, setBudgets] = useState([]);
  const [newBudget, setNewBudget] = useState({ category: '', amount: 0 });

  useEffect(() => {
    fetchBudgets();
  }, []);

  const fetchBudgets = async () => {
    try {
      const response = await api.get('/budgets');
      setBudgets(response.data);
    } catch (error) {
      console.error('Error fetching budgets:', error);
    }
  };

  const handleInputChange = (e) => {
    setNewBudget({ ...newBudget, [e.target.name]: e.target.value });
  };

  const handleCreateBudget = async () => {
    try {
      await api.post('/budgets', newBudget);
      setNewBudget({ category: '', amount: 0 });
      fetchBudgets();
    } catch (error) {
      console.error('Error creating budget:', error);
    }
  };

  const handleUpdateBudget = async (budget) => {
    try {
      await api.put(`/budgets/${budget.id}`, budget);
      fetchBudgets();
    } catch (error) {
      console.error('Error updating budget:', error);
    }
  };

  const handleDeleteBudget = async (budgetId) => {
    try {
      await api.delete(`/budgets/${budgetId}`);
      fetchBudgets();
    } catch (error) {
      console.error('Error deleting budget:', error);
    }
  };

  return (
    <div>
      <div>
        <input
          type="text"
          name="category"
          placeholder="Category"
          value={newBudget.category}
          onChange={handleInputChange}
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={newBudget.amount}
          onChange={handleInputChange}
        />
        <button onClick={handleCreateBudget}>Create Budget</button>
      </div>
      <ul>
        {budgets.map((budget) => (
          <li key={budget.id}>
            <span>{budget.category}</span>
            <span>{budget.amount}</span>
            <button onClick={() => handleUpdateBudget(budget)}>Update</button>
            <button onClick={() => handleDeleteBudget(budget.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BudgetManager;