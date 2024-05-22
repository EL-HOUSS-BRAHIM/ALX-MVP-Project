import React, { useState, useEffect } from 'react';
import '../styles/demo.css';

const DemoPage = () => {
  const [expenses, setExpenses] = useState([]);
  const [budgets, setBudgets] = useState([]);
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    const storedExpenses = JSON.parse(sessionStorage.getItem('expenses')) || [];
    const storedBudgets = JSON.parse(sessionStorage.getItem('budgets')) || [];
    const storedReminders = JSON.parse(sessionStorage.getItem('reminders')) || [];
    setExpenses(storedExpenses);
    setBudgets(storedBudgets);
    setReminders(storedReminders);
  }, []);

  useEffect(() => {
    sessionStorage.setItem('expenses', JSON.stringify(expenses));
    sessionStorage.setItem('budgets', JSON.stringify(budgets));
    sessionStorage.setItem('reminders', JSON.stringify(reminders));
  }, [expenses, budgets, reminders]);

  const addExpense = (expense) => setExpenses([...expenses, expense]);
  const deleteExpense = (index) => setExpenses(expenses.filter((_, i) => i !== index));

  const addBudget = (budget) => setBudgets([...budgets, budget]);
  const deleteBudget = (index) => setBudgets(budgets.filter((_, i) => i !== index));

  const addReminder = (reminder) => setReminders([...reminders, reminder]);
  const deleteReminder = (index) => setReminders(reminders.filter((_, i) => i !== index));

  return (
    <div className="demo-container">
      <h2>Demo Page</h2>
      <div className="mock-data">
        <section>
          <h3>Expenses</h3>
          <ul>
            {expenses.map((expense, index) => (
              <li key={index}>
                {expense} <button onClick={() => deleteExpense(index)}>Delete</button>
              </li>
            ))}
          </ul>
          <form onSubmit={(e) => { e.preventDefault(); addExpense(e.target.elements.expense.value); e.target.reset(); }}>
            <div>
              <input type="text" name="expense" placeholder="New Expense" required />
              <button type="submit">Add</button>
            </div>
          </form>
        </section>
        <section>
          <h3>Budgets</h3>
          <ul>
            {budgets.map((budget, index) => (
              <li key={index}>
                {budget} <button onClick={() => deleteBudget(index)}>Delete</button>
              </li>
            ))}
          </ul>
          <form onSubmit={(e) => { e.preventDefault(); addBudget(e.target.elements.budget.value); e.target.reset(); }}>
            <div>
              <input type="text" name="budget" placeholder="New Budget" required />
              <button type="submit">Add</button>
            </div>
          </form>
        </section>
        <section>
          <h3>Reminders</h3>
          <ul>
            {reminders.map((reminder, index) => (
              <li key={index}>
                {reminder} <button onClick={() => deleteReminder(index)}>Delete</button>
              </li>
            ))}
          </ul>
          <form onSubmit={(e) => { e.preventDefault(); addReminder(e.target.elements.reminder.value); e.target.reset(); }}>
            <div>
              <input type="text" name="reminder" placeholder="New Reminder" required />
              <button type="submit">Add</button>
            </div>
          </form>
        </section>
      </div>
    </div>
  );
};

export default DemoPage;
