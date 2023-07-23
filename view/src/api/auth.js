import axios from 'axios';

// api/auth.js

export async function loginAPI(username, password) {
  const response = await axios.post('http://localhost:5000/api/login', {
    username: username,
    password: password,
  });

  const token = response.data.token;

  // You can customize the response data according to your backend implementation
  return {
    user_data: response.data.user_data,
    token: token,
  };
}


export async function registerUserAPI(userData) {
  try {
    const response = await axios.post('http://localhost:5000/api/register', userData);

    // You can customize the response data according to your backend implementation
    return {
      username: response.data.username,
      token: response.data.token,
    };
  } catch (error) {
    console.log(error)
  }
}
