import api from './api';

const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
};

const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  return !!token;
};

export { setAuthToken, isAuthenticated };