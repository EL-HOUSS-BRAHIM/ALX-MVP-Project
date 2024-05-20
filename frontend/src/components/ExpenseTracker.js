import React, { useState, useEffect } from 'react';
import { addExpense, deleteExpense, getExpenses, updateExpense } from '../services/expense.service';

const ExpenseTracker = () => {
  const [expenses, setExpenses] = useState([]);
  const [newExpense, setNewExpense] = useState({
    name: '',
    amount: 0,
    category: '',
  });

  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const expenseData = await getExpenses();
        setExpenses(expenseData);
      } catch (error) {
        console.error('Error fetching expenses:', error);
      }
    };

    fetchExpenses();
  }, []);

  const handleCreateExpense = async (e) => {
    e.preventDefault();
    try {
      await addExpense(newExpense);
      setNewExpense({ name: '', amount: 0, category: '' });
      // Handle successful expense creation
    } catch (error) {
      console.error('Error creating expense:', error);
      // Handle error
    }
  };

  const handleDeleteExpense = async (expenseId) => {
    try {
      await deleteExpense(expenseId);
      const updatedExpenses = expenses.filter((expense) => expense.id !== expenseId);
      setExpenses(updatedExpenses);
      // Handle successful expense deletion
    } catch (error) {
      console.error('Error deleting expense:', error);
      // Handle error
    }
  };

  const handleUpdateExpense = async (updatedExpense) => {
    try {
      await updateExpense(updatedExpense);
      const updatedExpenses = expenses.map((expense) =>
        expense.id === updatedExpense.id ? updatedExpense : expense
      );
      setExpenses(updatedExpenses);
      // Handle successful expense update
    } catch (error) {
      console.error('Error updating expense:', error);
      // Handle error
    }
  };

  return (
    <div>
      <h2>Expense Tracker</h2>
      <form onSubmit={handleCreateExpense}>
        <input
          type="text"
          name="name"
          placeholder="Expense Name"
          value={newExpense.name}
          onChange={(e) => setNewExpense({ ...newExpense, name: e.target.value })}
          required
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={newExpense.amount}
          onChange={(e) => setNewExpense({ ...newExpense, amount: parseFloat(e.target.value) })}
          required
        />
        <input
          type="text"
          name="category"
          placeholder="Category"
          value={newExpense.category}
          onChange={(e) => setNewExpense({ ...newExpense, category: e.target.value })}
          required
        />
        <button type="submit">Add Expense</button>
      </form>
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            {expense.name} - {expense.amount} ({expense.category})
            <button onClick={() => handleDeleteExpense(expense.id)}>Delete</button>
            <button
              onClick={() =>
                handleUpdateExpense({ ...expense, amount: expense.amount + 100 })
              }
            >
              Increase
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExpenseTracker;