import { Helmet } from "react-helmet";
import ExpenseTracker from "../components/ExpenseTracker";
import "../styles/expenses.css";

const ExpenseTrackerPage = () => {
  return (
    <div className="expense-container">
      <Helmet>
        <title>Budget Management App - Expense Tracker</title>
        <meta
          name="description"
          content="Track your expenses and categorize them for better financial management."
        />
      </Helmet>
      <h1>Expense Tracker</h1>
      <ExpenseTracker />
    </div>
  );
};

export default ExpenseTrackerPage;