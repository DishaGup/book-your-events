
// store/action.js
import * as apievent from "../api/events";
import * as apiuser from "../api/auth";
import * as apimovie from '../api/movie'
import * as apishows from '../api/show'
export default {
  async login({ commit }, { username, password }) {
    try {
      const user = await apiuser.loginAPI(username, password);
     
      commit("setUser", user);
      // Save user data to local storage or use cookies, etc.
      localStorage.setItem("user", JSON.stringify(user));
    } catch (error) {
      alert("Invalid credentials. Please try again.");
      throw Error("Invalid credentials. Please try again.");
    }
  },

  async registerUser({ commit }, {userData}) {
    try {
      const user = await apiuser.registerUserAPI(userData);
      commit("setUser", user);
      // Save user data to local storage or use cookies, etc.
      localStorage.setItem("user", JSON.stringify(user));
    } catch (error) {
      // Handle error
      throw new Error("Failed to register user. Please try again.");
    }
  },

  async createEvent({ commit }, { eventData, config }) {
   
    try {
      const event = await apievent.createEventAPI(eventData, config);
    
      commit("addEvent", event);
      // Do something with the response, e.g., show a success message
    } catch (error) {
      console.log(error)
      throw new Error(error);
    }
  },
  async fetchEvents({ commit }) {
    try {
      const events = await apievent.fetchEventsAPI(); // Use api instead of event
     
      commit("setEvents", events.data.event);
    } catch (error) {
      // Handle error
    }
  },
  
  async bookevent({ commit }, { eventId, participantDetails }) {
    try {
      const events = await apievent.participateEventAPI(eventId, participantDetails);
   //   console.log(events)
      commit("setBookedEvents", events.data.event);
    } catch (error) {
      // Handle error
      console.error(error);
    }
  },
  async createMovie({ commit }, { movieData }) {
   // console.log(movieData)
    try {
      const event = await apimovie.createMovieAPI(movieData);
      //console.log(event)
      commit("addMovie", event);
      // Do something with the response, e.g., show a success message
    } catch (error) {
      console.log(error)
      throw new Error(error);
    }
  },
  async fetchSingleMovie({ commit }, movieId) {
    try {
      const movieData = await apimovie.getSingleMovieAPI(movieId);
      
      commit("setSingleMovie", movieData.data);
    } catch (error) {
      console.error("Error fetching single movie:", error);
      throw Error("Error fetching single movie. Please try again.");
    }
  },

  async fetchAllMovie({ commit }) {
    try {
      const movieData = await apimovie.getAllMovieAPI();
      //console.log(movieData)
      commit("setMovies", movieData.data.movies);
    } catch (error) {
      console.error("Error fetching single movie:", error);
      throw Error("Error fetching single movie. Please try again.");
    }
  },

  
async  fetchMovieShows({commit},movieId) {
  try {
    const showData = await apishows.getShowAPI(movieId);
    console.log(showData)
    commit("setShows", showData.data.shows);
  } catch (error) {
    console.error("Error fetching single movie:", error);
    throw Error("Error fetching single movie. Please try again.");
  }
  
}

};


