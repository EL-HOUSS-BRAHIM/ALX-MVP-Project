import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api'; // Replace with your backend API URL

export const getReminders = async (userId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/users/${userId}/reminders`);
    return response.data;
  } catch (error) {
    console.error('Error fetching reminders:', error);
    throw error;
  }
};

export const setReminder = async (userId, reminderData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/users/${userId}/reminders`, reminderData);
    return response.data;
  } catch (error) {
    console.error('Error setting reminder:', error);
    throw error;
  }
};

export const deleteReminder = async (userId, reminderId) => {
  try {
    const response = await axios.delete(`${API_BASE_URL}/users/${userId}/reminders/${reminderId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting reminder:', error);
    throw error;
  }
};