import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import BudgetManager from './pages/BudgetManager';
import ExpenseTracker from './pages/ExpenseTracker';
import ReminderManager from './pages/ReminderManager';

export const routes = [
  { path: '/', exact: true, component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/profile', component: Profile },
  { path: '/budget', component: BudgetManager },
  { path: '/expenses', component: ExpenseTracker },
  { path: '/reminders', component: ReminderManager },
];
