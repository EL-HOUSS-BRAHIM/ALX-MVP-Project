import { Helmet } from "react-helmet";
import AuthForm from "../components/AuthForm";
import "../styles/auth.css";

const Login = () => {
  return (
    <div className="auth-container">
      <Helmet>
        <title>Budget Management App - Login</title>
        <meta
          name="description"
          content="Log in to your Budget Management App account."
        />
      </Helmet>
      <h1>Login</h1>
      <AuthForm isLogin={true} />
    </div>
  );
};

export default Login;