import React, { useState, useEffect } from 'react';
import { Pie } from 'react-chartjs-2';
import expenseService from '../services/expense.service';
import '../styles/expenses.css';

const ExpenseChart = () => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    const fetchExpenses = async () => {
      const data = await expenseService.getExpenses();
      const categories = data.reduce((acc, expense) => {
        acc[expense.category] = (acc[expense.category] || 0) + expense.amount;
        return acc;
      }, {});
      setChartData({
        labels: Object.keys(categories),
        datasets: [
          {
            data: Object.values(categories),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#FF9F40', '#4BC0C0'],
          },
        ],
      });
    };
    fetchExpenses();
  }, []);

  return (
    <div className="expense-chart">
      <h3>Expense Chart</h3>
      <Pie data={chartData} />
    </div>
  );
};

export default ExpenseChart;
