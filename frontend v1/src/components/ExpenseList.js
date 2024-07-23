import React, { useState, useEffect } from 'react';
import expenseService from '../services/expense.service';
import '../styles/expenses.css';

const ExpenseList = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    const fetchExpenses = async () => {
      const data = await expenseService.getExpenses();
      setExpenses(data);
    };
    fetchExpenses();
  }, []);

  return (
    <div className="expense-list">
      <h3>Expenses</h3>
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            {expense.description}: ${expense.amount}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExpenseList;
