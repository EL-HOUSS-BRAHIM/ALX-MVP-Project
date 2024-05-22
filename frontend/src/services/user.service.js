import api from '../utils/api';

const userService = {
  getProfile: async () => {
    const response = await api.get('/user/profile');
    return response.data;
  }
};

export default userService;
