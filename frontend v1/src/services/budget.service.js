import api from '../utils/api';

const budgetService = {
  setBudget: async (budget) => {
    await api.post('/budget', { budget });
  },

  getBudgetSummary: async () => {
    const response = await api.get('/budget/summary');
    return response.data;
  }
};

export default budgetService;
