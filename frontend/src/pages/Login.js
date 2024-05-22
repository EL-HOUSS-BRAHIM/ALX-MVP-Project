import React from 'react';
import AuthForm from '../components/AuthForm';
import '../styles/auth.css';

const Login = () => {
  return (
    <div className="login-page">
      <AuthForm type="login" />
    </div>
  );
};

export default Login;
