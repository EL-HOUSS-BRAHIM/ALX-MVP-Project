// src/services/AuthService.js

import axios from 'axios';

const API_URL = 'http://localhost:5000/api/v1/auth/';

class AuthService {
    login(email, password) {
        return axios
            .post(API_URL + 'login', { email, password })
            .then(response => {
                if (response.data.access_token) {
                    localStorage.setItem('user', JSON.stringify(response.data));
                }
                return response.data;
            });
    }

    register(name, email, password) {
        return axios.post(API_URL + 'register', { name, email, password });
    }

    logout() {
        localStorage.removeItem('user');
    }

    getCurrentUser() {
        return JSON.parse(localStorage.getItem('user'));
    }
}

export default new AuthService();
