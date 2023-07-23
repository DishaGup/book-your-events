
import axios from "axios";

  export const getShowsAPI = (movieId) => {
    return axios.get(`http://localhost:5000/api/movies/${movieId}/shows`);
  };
  
