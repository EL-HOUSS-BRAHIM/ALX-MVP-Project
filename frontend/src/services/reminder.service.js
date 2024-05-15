import axios from 'axios';

const API_URL = '/api/reminders';

const setReminder = async (reminderData) => {
  try {
    const response = await axios.post(`${API_URL}`, reminderData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const getReminders = async () => {
  try {
    const response = await axios.get(`${API_URL}`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

const deleteReminder = async (reminderId) => {
  try {
    await axios.delete(`${API_URL}/${reminderId}`);
  } catch (error) {
    throw error.response.data;
  }
};

export { setReminder, getReminders, deleteReminder };