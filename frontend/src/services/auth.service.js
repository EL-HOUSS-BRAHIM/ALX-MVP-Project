import api from '../utils/api';

const authService = {
  login: async (credentials) => {
    const response = await api.post('/auth/login', credentials);
    localStorage.setItem('user', JSON.stringify(response.data));
  },

  register: async (credentials) => {
    const response = await api.post('/auth/register', credentials);
    localStorage.setItem('user', JSON.stringify(response.data));
  },

  logout: () => {
    localStorage.removeItem('user');
  },

  isAuthenticated: () => {
    return localStorage.getItem('user') !== null;
  }
};

export default authService;
