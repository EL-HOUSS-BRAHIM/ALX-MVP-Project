import axios from 'axios';

const API_URL = '/api/expenses';

const addExpense = async (expenseData) => {
  try {
    const response = await axios.post(`${API_URL}`, expenseData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getExpenses = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const updateExpense = async (expenseId, expenseData) => {
  try {
    const response = await axios.put(`${API_URL}/${expenseId}`, expenseData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const deleteExpense = async (expenseId) => {
  try {
    await axios.delete(`${API_URL}/${expenseId}`);
  } catch (error) {
    throw error.response.data;
  }
};

export { addExpense, getExpenses, updateExpense, deleteExpense };