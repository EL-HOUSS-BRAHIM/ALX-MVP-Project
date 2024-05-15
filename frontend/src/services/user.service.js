import axios from 'axios';

const API_URL = '/api/users';

const getUserProfile = async () => {
  try {
    const response = await axios.get(`${API_URL}/profile`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const updateUserProfile = async (userData) => {
  try {
    const response = await axios.put(`${API_URL}/profile`, userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export { getUserProfile, updateUserProfile };