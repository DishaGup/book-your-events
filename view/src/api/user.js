import axios from 'axios';

// User login
export const login = (userData) => {
  return axios.post('/login', userData);
};

// User registration
export const register = (userData) => {
  return axios.post('/register', userData);
};
