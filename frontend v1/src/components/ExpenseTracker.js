// components/ExpenseTracker.js
import React, { useState, useEffect } from 'react';
import api from '../utils/api';

const ExpenseTracker = () => {
  const [expenses, setExpenses] = useState([]);
  const [newExpense, setNewExpense] = useState({ description: '', amount: 0, category: '' });

  useEffect(() => {
    fetchExpenses();
  }, []);

  const fetchExpenses = async () => {
    try {
      const response = await api.get('/expenses');
      setExpenses(response.data);
    } catch (error) {
      console.error('Error fetching expenses:', error);
    }
  };

  const handleInputChange = (e) => {
    setNewExpense({ ...newExpense, [e.target.name]: e.target.value });
  };

  const handleCreateExpense = async () => {
    try {
      await api.post('/expenses', newExpense);
      setNewExpense({ description: '', amount: 0, category: '' });
      fetchExpenses();
    } catch (error) {
      console.error('Error creating expense:', error);
    }
  };

  const handleUpdateExpense = async (expense) => {
    try {
      await api.put(`/expenses/${expense.id}`, expense);
      fetchExpenses();
    } catch (error) {
      console.error('Error updating expense:', error);
}
};

const handleDeleteExpense = async (expenseId) => {
try {
  await api.delete(`/expenses/${expenseId}`);
  fetchExpenses();
} catch (error) {
  console.error('Error deleting expense:', error);
}
};

return (
<div>
  <div>
    <input
      type="text"
      name="description"
      placeholder="Description"
      value={newExpense.description}
      onChange={handleInputChange}
    />
    <input
      type="number"
      name="amount"
      placeholder="Amount"
      value={newExpense.amount}
      onChange={handleInputChange}
    />
    <input
      type="text"
      name="category"
      placeholder="Category"
      value={newExpense.category}
      onChange={handleInputChange}
    />
    <button onClick={handleCreateExpense}>Add Expense</button>
  </div>
  <ul>
    {expenses.map((expense) => (
      <li key={expense.id}>
        <span>{expense.description}</span>
        <span>{expense.amount}</span>
        <span>{expense.category}</span>
        <button onClick={() => handleUpdateExpense(expense)}>Update</button>
        <button onClick={() => handleDeleteExpense(expense.id)}>Delete</button>
      </li>
    ))}
  </ul>
</div>
);
};

export default ExpenseTracker;