import axios from 'axios';

// Fetch all events
export const fetchEvents = () => {
  return axios.get('/events');
};

// Make a POST request to participate in an event
export const participateEvent = (eventId) => {
  return axios.post(`/events/${eventId}/participate`);
};
