import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser, logoutUser, registerUser } from '../services/auth.service';

const AuthForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });
  const [isLogin, setIsLogin] = useState(true);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await (isLogin ? loginUser(formData) : registerUser(formData));
      // Handle successful authentication
      navigate('/dashboard'); // Replace '/dashboard' with the desired route
    } catch (error) {
      console.error('Authentication error:', error);
      // Handle authentication error
    }
  };

  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
    setFormData({ email: '', password: '' });
  };

  return (
    <div>
      <h2>{isLogin ? 'Login' : 'Register'}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
      </form>
      <button onClick={toggleAuthMode}>
        {isLogin ? 'Create an account' : 'Already have an account?'}
      </button>
    </div>
  );
};

export default AuthForm;