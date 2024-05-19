import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import BudgetManager from './pages/BudgetManager';
import ExpenseTracker from './pages/ExpenseTracker';
import ReminderManager from './pages/ReminderManager';
import PlanPricesPage from './components/PlanPricesPage';
import TesterPlanPage from './components/TesterPlanPage';
import ComingSoonPage from './components/ComingSoonPage';
import LandingPage from './components/LandingPage';

export const routes = [
  { path: '/', exact: true, component: Home },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/profile', component: Profile, protected: true },
  { path: '/budget', component: BudgetManager, protected: true },
  { path: '/expenses', component: ExpenseTracker, protected: true },
  { path: '/reminders', component: ReminderManager, protected: true },
  { path: '/plans', component: PlanPricesPage },
  { path: '/tester', component: TesterPlanPage },
  { path: '/coming-soon', component: ComingSoonPage },
  { path: '/landing', component: LandingPage },
];
