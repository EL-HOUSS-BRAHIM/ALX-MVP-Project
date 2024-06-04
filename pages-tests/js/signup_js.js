document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
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

    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Mock user data for demonstration
        const mockUserData = [
            { name: 'John Doe', email: 'john@example.com', password: 'password123' },
            { name: 'Jane Smith', email: 'jane@example.com', password: 'qwerty456' }
        ];

        // Check if the user already exists (mock implementation)
        const existingUser = mockUserData.find(user => user.email === email);
        if (existingUser) {
            errorMessage.textContent = 'User with this email already exists. Please log in or use a different email.';
            errorMessage.style.display = 'block';
            successMessage.style.display = 'none';
        } else {
            errorMessage.style.display = 'none';
            successMessage.textContent = 'Sign up successful! Redirecting to login...';
            successMessage.style.display = 'block';
            mockUserData.push({ name, email, password }); // Mock adding user to database
            setTimeout(() => {
                window.location.href = 'login.html'; // Redirect after 2 seconds
            }, 2000);
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