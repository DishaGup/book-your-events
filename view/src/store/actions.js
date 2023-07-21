import * as api from '../api/events';
// Import necessary API functions for fetching events, logging in, etc.
//import { fetchEventsAPI, loginAPI, participateEventAPI } from '../api';

export default {
  async fetchEvents({ commit }) {
    try {
      const events = await fetchEventsAPI();
      commit('setEvents', events);
    } catch (error) {
      // Handle error
    }
  },
  async login({ commit }, { username, password }) {
    try {
      const user = await loginAPI(username, password);
      commit('setUser', user);
      // Save user data to local storage or use cookies, etc.
    } catch (error) {
      // Handle error
    }
  },
  async participateEvent({ commit }, eventId) {
    try {
      const response = await api.participateEvent(eventId);
      // Do something with the response, e.g., show a success message
    } catch (error) {
      // Handle error
    }
  },
  // Add more actions as needed
};

 
