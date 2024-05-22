import api from '../utils/api';

const reminderService = {
  getReminders: async () => {
    const response = await api.get('/reminders');
    return response.data;
  },

  addReminder: async (reminder) => {
    await api.post('/reminders', reminder);
  }
};

export default reminderService;
