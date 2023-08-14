
import axios from "axios";

  export const getShowsAPI = (movieId) => {
    return axios.get(`http://localhost:5000/api/movies/${movieId}/shows`);
  };
  

  export const AddParticipantShowAPI = (bookingData) => {
    return axios.post(`http://localhost:5000/api/book_show`,bookingData);
  };
  
  export const addShowTimingsAPI = (movieId, showTimingsData) =>
  axios.post(`http://localhost:5000/api/movies/${movieId}/shows`, showTimingsData);

  
export const removeShowTimingAPI = (movieId, showId) =>
axios.delete(`http://localhost:5000/api/movies/${movieId}/shows/${showId}`);
