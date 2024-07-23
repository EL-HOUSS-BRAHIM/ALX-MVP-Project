import React from 'react';
import AuthForm from '../components/AuthForm';
import '../styles/auth.css';

const Register = () => {
  return (
    <div className="register-page">
      <AuthForm type="register" />
    </div>
  );
};

export default Register;
