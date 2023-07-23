
// api/events.js
import axios from "axios";

// Fetch all events
export const fetchEventsAPI = () => {
  return axios.get("http://localhost:5000/api/events");
};

export const participateEventAPI = (eventId,participantDetails) => {
  return axios.post(`http://localhost:5000/api/events/book`, { eventId ,participantDetails });
};

export const createEventAPI = (eventDetails, config) => {
  return axios.post(`http://localhost:5000/api/events`, eventDetails, config);
};
