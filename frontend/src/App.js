import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './pages/Layout';
import Home from './pages/Home';
import BudgetManagerPage from './pages/BudgetManager';
import ExpenseTrackerPage from './pages/ExpenseTracker';
import ReminderManagerPage from './pages/ReminderManager';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import Contact from './pages/Contact';
import NoPage from './pages/NoPage';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route path="home" index element={<Home />} />
          <Route path="budget" element={<ProtectedRoute><BudgetManagerPage /></ProtectedRoute>} />
          <Route path="expenses" element={<ProtectedRoute><ExpenseTrackerPage /></ProtectedRoute>} />
          <Route path="reminders" element={<ProtectedRoute><ReminderManagerPage /></ProtectedRoute>} />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
          <Route path="contact" element={<Contact />} />
          <Route path="about" element={<About />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;