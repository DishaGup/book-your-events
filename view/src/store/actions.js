// store/action.js
import * as apievent from "../api/events";
import * as apiuser from "../api/auth";
import * as apimovie from "../api/movie";
import * as apishows from "../api/show";

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

  async registerUser( _,{ userData }) {
    try {
      //console.log(userData)
      const user = await apiuser.registerUserAPI(userData);
      console.log(user)
//commit("setUser", user);
      // Save user data to local storage or use cookies, etc.
     //localStorage.setItem("user", JSON.stringify(user));
    } catch (error) {
      console.log(error)
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
      console.log(error);
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
      const events = await apievent.participateEventAPI(
        eventId,
        participantDetails
      );
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
      console.log(error);
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

  async fetchMovieShows({ commit }, movieId) {
    try {
      const showData = await apishows.getShowsAPI(movieId);
     // console.log(showData);
      commit("setShows", showData.data.shows);
    } catch (error) {
      console.error("Error fetching single movie:", error);
      throw Error("Error fetching single movie. Please try again.");
    }
  },

  async addShowTimingAction(_, { movieId, data }) {
    try {
      console.log(movieId,data)
      const response = await apishows.addShowTimingsAPI(movieId, data);
      console.log(response)
    //  commit("setShows", response.data.shows);
    } catch (error) {
      console.error("Error adding show timings:", error);
      throw error;
    }
  },  

  

  async bookMovieShow({ commit }, { movieId, participantData }) {
    try {
      const bookingData = {
        movieId: movieId,
        participant: participantData,
      };
      const data = await apishows.AddParticipantShowAPI(bookingData);
      console.log("Booking success:", data);
      commit("setBookedMovies", data.data.movies);
      // Handle success, show confirmation message or navigate to confirmation page
    } catch (error) {
      console.error("Error booking show:", error);
      // Handle error, show error message to the user
      throw Error("Error booking show. Please try again.");
    }
  },

  
  // Action to remove a show timing
  removeShowTiming({ commit }, index) {
    commit('removeNewShowTiming', index);
  },
};
