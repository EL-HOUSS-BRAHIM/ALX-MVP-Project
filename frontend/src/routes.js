import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import ExpenseTracker from './pages/ExpenseTracker';
import BudgetManager from './pages/BudgetManager';
import ReminderManager from './pages/ReminderManager';
import PrivateRoute from './components/PrivateRoute';

const Routes = () => (
  <Router>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/login" component={Login} />
      <Route path="/register" component={Register} />
      <PrivateRoute path="/profile" component={Profile} />
      <PrivateRoute path="/expenses" component={ExpenseTracker} />
      <PrivateRoute path="/budget" component={BudgetManager} />
      <PrivateRoute path="/reminders" component={ReminderManager} />
    </Switch>
  </Router>
);

export default Routes;