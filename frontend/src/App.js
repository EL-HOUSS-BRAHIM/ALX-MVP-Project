import React, { useEffect } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { setAuthToken } from './utils/auth';
import Routes from './routes';
import Header from './components/Header';
import Footer from './components/Footer';

const App = () => {
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setAuthToken(token);
    }
  }, []);

  return (
    <Router>
      <Header />
      <Routes />
      <Footer />
    </Router>
  );
};

export default App;