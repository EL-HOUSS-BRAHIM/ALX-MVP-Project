import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import budgetService from '../services/budget.service';
import '../styles/budget.css';

const BudgetChart = () => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    const fetchSummary = async () => {
      const data = await budgetService.getBudgetSummary();
      setChartData({
        labels: data.labels,
        datasets: [
          {
            label: 'Expenses',
            data: data.expenses,
            fill: false,
            backgroundColor: '#FF6384',
            borderColor: '#FF6384',
          },
          {
            label: 'Budget',
            data: data.budget,
            fill: false,
            backgroundColor: '#36A2EB',
            borderColor: '#36A2EB',
          },
        ],
      });
    };
    fetchSummary();
  }, []);

  return (
    <div className="budget-chart">
      <h3>Budget Chart</h3>
      <Line data={chartData} />
    </div>
  );
};

export default BudgetChart;
