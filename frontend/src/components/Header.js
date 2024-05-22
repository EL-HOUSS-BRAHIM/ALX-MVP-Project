import React from 'react';
import logo from '../assets/logo.png'; // Replace with your logo file path

const Header = () => {
  return (
    <header>
      <nav>
        <div className="logo">
          <a href="#">
            <img src={logo} alt="Logo" />
          </a>
        </div>
      </nav>
    </header>
  );
};

export default Header;