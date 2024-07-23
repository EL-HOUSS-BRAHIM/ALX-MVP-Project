import api from '../utils/api';

const expenseService = {
  getExpenses: async () => {
    const response = await api.get('/expenses');
    return response.data;
  },

  addExpense: async (expense) => {
    await api.post('/expenses', expense);
  }
};

export default expenseService;
