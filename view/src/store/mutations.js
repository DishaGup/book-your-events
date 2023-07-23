//store/mutation.js

export default {
  setEvents(state, Allevents) {
    state.Allevents = Allevents;
  },
  setUser(state, user) {
    state.user = user;
  },
  addEvent(state, Allevents) {
    state.Allevents.push(Allevents);
  },
  setBookedEvents(state,bookedevents){
    state.bookedevents=bookedevents
  },
  setMovies(state, Allmovies) {
    state.Allmovies = Allmovies;
  },
  addMovie(state, Allmovies) {
    state.Allmovies.push(Allmovies);
  },
  
  setSingleMovie(state, movieData) {
    state.singlemovie = movieData;
  },
  setShows(state, shows) {
    state.shows = shows;
  },
};
