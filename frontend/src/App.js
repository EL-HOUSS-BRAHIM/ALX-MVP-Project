import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import { routes } from './routes';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Switch>
        {routes.map((route, index) => (
          route.protected ? (
            <ProtectedRoute
              key={index}
              path={route.path}
              exact={route.exact}
              component={route.component}
            />
          ) : (
            <Route
              key={index}
              path={route.path}
              exact={route.exact}
              component={route.component}
            />
          )
        ))}
      </Switch>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
