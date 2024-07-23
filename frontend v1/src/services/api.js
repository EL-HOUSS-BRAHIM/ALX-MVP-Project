const API_URL = 'http://localhost:5000/api/v1';

export const fetchFromAPI = async (endpoint, method = 'GET', body) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    method,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }

  return response.json();
};
