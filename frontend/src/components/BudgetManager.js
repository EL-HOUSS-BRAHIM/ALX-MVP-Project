import React, { useState } from 'react';

const BudgetManager = ({ budgetData, onBudgetUpdate }) => {
  const [totalBudget, setTotalBudget] = useState(budgetData.totalBudget);
  const [categories, setCategories] = useState(budgetData.categories);

  const handleBudgetChange = (event) => {
    setTotalBudget(parseFloat(event.target.value));
    onBudgetUpdate({ ...budgetData, totalBudget: parseFloat(event.target.value) });
  };

  const handleCategoryChange = (index, event) => {
    const newCategories = [...categories];
    newCategories[index].amount = parseFloat(event.target.value);
    setCategories(newCategories);
    onBudgetUpdate({ ...budgetData, categories: newCategories });
  };

  return (
    <div>
      <label htmlFor="totalBudget">Total Budget:</label>
      <input
        type="number"
        id="totalBudget"
        value={totalBudget}
        onChange={handleBudgetChange}
      />

      <h3>Categories:</h3>
      <ul>
        {categories.map((category, index) => (
          <li key={index}>
            <label htmlFor={`category-${index}`}>{category.name}:</label>
            <input
              type="number"
              id={`category-${index}`}
              value={category.amount}
              onChange={(event) => handleCategoryChange(index, event)}
            />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BudgetManager;