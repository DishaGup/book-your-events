import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/HomePage.vue';
import Events from './views/EventPage.vue';
import Bookings from './views/BookingPage.vue';
import Login from './views/LoginForm.vue';
import Register from './views/RegisterPage.vue'
import CreateEvent from './views/CreateEventPage.vue'
// Set the base URL for API requests
axios.defaults.baseURL = 'http://localhost:5000/api';

// Add an Axios request interceptor to set the JWT token in headers
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

// Define Vue Router routes
const routes = [
  { path: '/', component: Home },
  { path: '/events', component: Events },
  { path: '/bookings', component: Bookings },
  {path:'/login' ,component: Login },
  {path:'/register' ,component: Register },
  {path:'/create-event',component:CreateEvent }

  // Add more routes for other pages as needed
];

// Create Vue Router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Create the Vue app instance with the router and mount it to the app div
const app = createApp(App);
app.use(router);
app.mount('#app');
