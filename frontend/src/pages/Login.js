import React, { useState } from 'react';
import AuthForm from '../components/AuthForm';
import { loginUser } from '../services/auth.service';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      await loginUser({ email, password });
      // Redirect to the appropriate page after successful login
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <AuthForm
        email={email}
        setEmail={setEmail}
        password={password}
        setPassword={setPassword}
        handleSubmit={handleLogin}
        submitText="Login"
      />
    </div>
  );
};

export default Login;