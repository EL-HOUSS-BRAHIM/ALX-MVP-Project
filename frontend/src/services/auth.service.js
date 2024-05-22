import axios from 'axios';

const API_URL = '/api/v1/auth';

const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}/register`, userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}`, credentials);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const logoutUser = async () => {
  try {
    await axios.post(`${API_URL}/logout`);
  } catch (error) {
    throw error.response.data;
  }
};

export { registerUser, loginUser, logoutUser };