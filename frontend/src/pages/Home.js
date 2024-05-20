import { Helmet } from "react-helmet";
import "../styles/home.css";

const Home = () => {
  return (
    <div className="home-container">
      <Helmet>
        <title>Budget Management App - Home</title>
        <meta
          name="description"
          content="Manage your finances, track expenses, and set reminders with ease."
        />
      </Helmet>
      <div className="hero-section">
        <h1>Welcome to the Budget Management App</h1>
        <p>
          Stay on top of your finances by creating budgets, tracking expenses,
          and setting reminders for important events or bills.
        </p>
        <button className="cta-button">Get Started</button>
      </div>
      <div className="features-section">
        <h2>Features</h2>
        <ul>
          <li>Create and manage multiple budgets</li>
          <li>Track your expenses by category</li>
          <li>Set reminders for bills, events, and tasks</li>
          <li>Personalized dashboard and analytics</li>
        </ul>
      </div>
    </div>
  );
};

export default Home;