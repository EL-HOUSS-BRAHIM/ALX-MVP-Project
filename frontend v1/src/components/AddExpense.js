import React, { useState } from 'react';
import expenseService from '../services/expense.service';
import '../styles/expenses.css';

const AddExpense = () => {
  const [expense, setExpense] = useState({ description: '', amount: '' });

  const handleChange = (e) => {
    setExpense({ ...expense, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await expenseService.addExpense(expense);
      // Optionally reset form and/or show success message
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="add-expense">
      <h3>Add Expense</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="description"
          placeholder="Description"
          value={expense.description}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount"
          value={expense.amount}
          onChange={handleChange}
          required
        />
        <button type="submit">Add Expense</button>
      </form>
    </div>
  );
};

export default AddExpense;
