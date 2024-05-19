import React, { useEffect, useState } from 'react';
import { getBudgets, createBudget, updateBudget, deleteBudget } from '../services/budget.service';

const BudgetManager = () => {
  const [budgets, setBudgets] = useState([]);
  const [newBudgetName, setNewBudgetName] = useState('');
  const [newBudgetAmount, setNewBudgetAmount] = useState(0);

  useEffect(() => {
    fetchBudgets();
  }, []);

  const fetchBudgets = async () => {
    try {
      const budgetsData = await getBudgets();
      setBudgets(budgetsData);
    } catch (error) {
      console.error('Error fetching budgets:', error);
    }
  };

  const handleCreateBudget = async () => {
    try {
      await createBudget(newBudgetName, newBudgetAmount);
      setNewBudgetName('');
      setNewBudgetAmount(0);
      fetchBudgets();
    } catch (error) {
      console.error('Error creating budget:', error);
    }
  };

  const handleUpdateBudget = async (budgetId, updates) => {
    try {
      await updateBudget(budgetId, updates);
      fetchBudgets();
    } catch (error) {
      console.error('Error updating budget:', error);
    }
  };

  const handleDeleteBudget = async (budgetId) => {
    try {
      await deleteBudget(budgetId);
      fetchBudgets();
    } catch (error) {
      console.error('Error deleting budget:', error);
    }
  };

  return (
    <div>
      <h2>Budgets</h2>
      <ul>
        {budgets.map((budget) => (
          <li key={budget.id}>
            <h3>{budget.name}</h3>
            <p>Amount: {budget.amount}</p>
            <button onClick={() => handleUpdateBudget(budget.id, { amount: budget.amount + 100 })}>
              Increase Amount
            </button>
            <button onClick={() => handleDeleteBudget(budget.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <h3>Create New Budget</h3>
      <input
        type="text"
        placeholder="Budget Name"
        value={newBudgetName}
        onChange={(e) => setNewBudgetName(e.target.value)}
      />
      <input
        type="number"
        placeholder="Budget Amount"
        value={newBudgetAmount}
        onChange={(e) => setNewBudgetAmount(parseFloat(e.target.value))}
      />
      <button onClick={handleCreateBudget}>Create Budget</button>
    </div>
  );
};

export default BudgetManager;
