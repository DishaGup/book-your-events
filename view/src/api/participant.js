
import axios from "axios";

  export const getParticipantsAPI = (movieId) => {
    return axios.get(`http://localhost:5000/api/movies/${movieId}/shows`);
  };
  

