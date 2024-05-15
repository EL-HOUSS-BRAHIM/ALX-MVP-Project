const formatCurrency = (value) => {
    return `$${value.toFixed(2)}`;
  };
  
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };
  
  const checkJWTExpiration = (token) => {
    // Implement JWT expiration check logic here
    // Return true if the token is valid, false otherwise
    return true; // Placeholder implementation
  };
  
  export { formatCurrency, formatDate, checkJWTExpiration };