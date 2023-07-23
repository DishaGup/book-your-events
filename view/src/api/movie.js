
import axios from "axios";

export const fetchMoviesAPI = () => {
    return axios.get("http://localhost:5000/api/movies");
  };
  
  export const participateMovieAPI = (eventId,participantDetails) => {
    return axios.post(`http://localhost:5000/api/movies/book`, { eventId ,participantDetails });
  };
  
  export const createMovieAPI = (eventDetails) => {
    return axios.post(`http://localhost:5000/api/movies`, eventDetails);
  };
  
  export const getSingleMovieAPI = (movieId) => {
    return axios.get(`http://localhost:5000/api/movies/${movieId}`);
  };
  
  export const getAllMovieAPI = () => {
    return axios.get(`http://localhost:5000/api/movies`);
  };
  
