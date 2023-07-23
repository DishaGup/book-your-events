import {createApp} from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/HomePage.vue';
import Events from './views/EventPage.vue';
import Bookings from './views/BookingPage.vue';
import Login from './views/LoginForm.vue';
import Register from './views/RegisterPage.vue';
import CreateEvent from './views/CreateEventPage.vue'
import AddMovie from './views/AddMovieForm.vue'
import store from './store/index.js';
import SingleMoviePage from '@/views/SingleMoviePage.vue';
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
  { path: '/', component: Home   },
  { path: '/events', component: Events,meta: { fromHistory: true }  },
  { path: '/bookings', component: Bookings ,meta: { fromHistory: true }  },
  { path: '/login', component: Login  },
  { path: '/register', component: Register },
  { 
    path: '/create-event', 
    component: CreateEvent,
    // Add the beforeEnter guard
  //   beforeEnter: (to, from, next) => {
  //     const user = JSON.parse(localStorage.getItem('user'));
  //     if (!user || user.user_data.role !== 'admin') {
  //       // Redirect to login if user is not logged in or not an admin
  //       next('/login');
  //     } else {
  //       // Allow access to the CreateEventPage for logged-in admins
  //       next();
  //     }
  //   }
   },
  // Add more routes for other pages as needed

  { path: '/create-movie', component: AddMovie },
  {
    path: '/movie/:id',
    name: 'singleMovie',
    component: SingleMoviePage,
  },


];

// Create Vue Router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Create the Vue app instance with the router and mount it to the app div
const vueApp = createApp(App);
vueApp.use(router);
vueApp.use(store);
vueApp.mount('#app');
