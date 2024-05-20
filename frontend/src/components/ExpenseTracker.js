import React, { useEffect, useState } from "react";
import {
  getExpenses,
  createExpense,
  updateExpense,
  deleteExpense,
} from "../services/expense.service";

const ExpenseTracker = () => {
  const [expenses, setExpenses] = useState([]);
  const [newExpenseName, setNewExpenseName] = useState("");
  const [newExpenseAmount, setNewExpenseAmount] = useState(0);

  useEffect(() => {
    fetchExpenses();
  }, []);

  const fetchExpenses = async () => {
    try {
      const expensesData = await getExpenses();
      setExpenses(expensesData);
    } catch (error) {
      console.error("Error fetching expenses:", error);
    }
  };

  const handleCreateExpense = async () => {
    try {
      await createExpense(newExpenseName, newExpenseAmount);
      setNewExpenseName("");
      setNewExpenseAmount(0);
      fetchExpenses();
    } catch (error) {
      console.error("Error creating expense:", error);
    }
  };

  const handleUpdateExpense = async (expenseId, updates) => {
    try {
      await updateExpense(expenseId, updates);
      fetchExpenses();
    } catch (error) {
      console.error("Error updating expense:", error);
    }
  };

  const handleDeleteExpense = async (expenseId) => {
    try {
      await deleteExpense(expenseId);
      fetchExpenses();
    } catch (error) {
      console.error("Error deleting expense:", error);
    }
  };

  return (
    <div>
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            <h3>{expense.name}</h3>
            <p>Amount: {expense.amount}</p>
            <button onClick={() => handleUpdateExpense(expense.id, { amount: expense.amount + 10 })}>
              Increase Amount
            </button>
            <button onClick={() => handleDeleteExpense(expense.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <h3>Create New Expense</h3>
      <input
        type="text"
        placeholder="Expense Name"
        value={newExpenseName}
        onChange={(e) => setNewExpenseName(e.target.value)}
      />
      <input
        type="number"
        placeholder="Expense Amount"
        value={newExpenseAmount}
        onChange={(e) => setNewExpenseAmount(parseFloat(e.target.value))}
      />
      <button onClick={handleCreateExpense}>Create Expense</button>
    </div>
  );
};

export default ExpenseTracker;