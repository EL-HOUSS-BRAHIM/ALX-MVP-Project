document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const errorMessage = document.getElementById('error-message');
  const successMessage = document.getElementById('success-message');
  const authLinks = document.getElementById('auth-links');

  // Function to check if the user is logged in (mock implementation)
  const isLoggedIn = () => {
    return localStorage.getItem('userLoggedIn') === 'true';
  };

  // Update navigation links based on login status
  const updateNavLinks = () => {
    if (isLoggedIn()) {
      authLinks.innerHTML = '<a href="#" id="logout-link">Logout</a>';
    } else {
      authLinks.innerHTML = '<a href="login.html">Login</a> | <a href="signup.html">Sign Up</a>';
    }
  };

  // Call the function to update the navigation on page load
  updateNavLinks();

  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Mock login data for demonstration
    const mockUserData = {
      email: 'test@example.com',
      password: 'password123'
    };

    if (email === mockUserData.email && password === mockUserData.password) {
      errorMessage.style.display = 'none';
      successMessage.textContent = 'Login successful! Redirecting to dashboard...';
      successMessage.style.display = 'block';
      localStorage.setItem('userLoggedIn', 'true'); // Set user as logged in
      updateNavLinks(); // Update nav links after login
      setTimeout(() => {
        window.location.href = 'dashboard.html'; // Redirect after 2 seconds
      }, 2000);
    } else {
      successMessage.style.display = 'none';
      errorMessage.textContent = 'Invalid email or password. Please try again.';
      errorMessage.style.display = 'block';
    }
  });

  // Handle logout
  document.addEventListener('click', (e) => {
    if (e.target && e.target.id === 'logout-link') {
      e.preventDefault();
      localStorage.removeItem('userLoggedIn'); // Remove login status
      successMessage.textContent = 'You have been logged out.';
      successMessage.style.display = 'block';
      errorMessage.style.display = 'none';
      updateNavLinks(); // Update nav links after logout
      setTimeout(() => {
        window.location.href = 'login.html'; // Redirect after 2 seconds
      }, 2000);
    }
  });
});
// Get the toggle menu button and navigation menu elements
const toggleMenu = document.querySelector('.toggle-menu');
const navMenu = document.querySelector('header nav');

// Add a click event listener to the toggle menu button
toggleMenu.addEventListener('click', () => {
  // Toggle the 'active' class on the toggle menu button and navigation menu
  toggleMenu.classList.toggle('active');
  navMenu.classList.toggle('active');
});
