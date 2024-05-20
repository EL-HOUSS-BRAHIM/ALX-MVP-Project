import { Helmet } from "react-helmet";
import BudgetManager from "../components/BudgetManager";
import "../styles/budget.css";

const BudgetManagerPage = () => {
  return (
    <div className="budget-container">
      <Helmet>
        <title>Budget Management App - Budget Manager</title>
        <meta
          name="description"
          content="Create and manage your budgets for different categories."
        />
      </Helmet>
      <h1>Budget Manager</h1>
      <BudgetManager />
    </div>
  );
};

export default BudgetManagerPage;