import React, { useState } from 'react';
import AuthForm from '../components/AuthForm';
import { registerUser } from '../services/auth.service';

const Register = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    try {
      await registerUser({ email, password });
      // Redirect to the appropriate page after successful registration
    } catch (error) {
      console.error('Registration failed:', error);
    }
  };

  return (
    <div>
      <h1>Register</h1>
      <AuthForm
        email={email}
        setEmail={setEmail}
        password={password}
        setPassword={setPassword}
        handleSubmit={handleRegister}
        submitText="Register"
      />
    </div>
  );
};

export default Register;