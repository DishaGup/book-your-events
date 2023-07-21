<!-- src/components/LoginForm.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/api/login', {
            username: this.username,
            password: this.password,
          });
          const token = response.data.token;
  
          // Save the token to local storage or use a state management library like Vuex
          localStorage.setItem('token', token);
  
          // Redirect to the dashboard or another page
          // For demonstration purposes, let's simply log in the console
          console.log('Logged in successfully!');
  
          // You can use Vue Router to navigate to another page if needed
        } catch (error) {
          console.error('Login failed:', error.response.data.message);
        }
      },
    },
  };
  </script>
  