import axios from 'axios';

const API_URL = '/api/budgets';

const setBudget = async (budgetData) => {
  try {
    const response = await axios.post(`${API_URL}`, budgetData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getBudgetSummary = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const updateBudget = async (budgetId, budgetData) => {
  try {
    const response = await axios.put(`${API_URL}/${budgetId}`, budgetData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const deleteBudget = async (budgetId) => {
  try {
    await axios.delete(`${API_URL}/${budgetId}`);
  } catch (error) {
    throw error.response.data;
  }
};

export { setBudget, getBudgetSummary, updateBudget, deleteBudget };