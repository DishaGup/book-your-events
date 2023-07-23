<template>
  <div class="event-card">
    <h3>{{ event.eventName }}</h3>
    <p>{{ formatDate(event.eventDate) }}</p>
    <p>Category: {{ event.category }}</p>
    <p>Venue: {{ event.venue }}</p>
    <p>Ticket Price: {{ event.ticket_price }}</p>
    <p>Location: {{ event.location }}</p>
    <button @click="onBookEvent">Book Now</button>
    <ParticipantForm v-if="showParticipantForm" @book-event="onBookEventCompleted" />

  </div>
</template>

<script>
import ParticipantForm from "@/components/ParticipantForm.vue"; // Replace with the correct path

export default {

  components: {
    ParticipantForm,
  },
  data() {
    return {
      showParticipantForm: false,
    };
  },
  props: {
    event: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onBookEvent() {
      // Check if user is logged in
      if (!this.$store.state.user) {
        alert("Please log in before booking an event.");
        // You may redirect the user to the login page here if desired
        return;
      }

      this.showParticipantForm = true;
    },
    onBookEventCompleted(participantDetails) {
      // Hide the participant form overlay
      this.showParticipantForm = false;
      // You can implement a modal or a form overlay to collect participant details

      // After collecting the participant details, call the bookevent action
      this.$store.dispatch("bookevent", { eventId: this.event._id, participantDetails });
    },
    formatDate(dateString) {
      const eventDate = new Date(dateString);
  const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  };
  return eventDate.toLocaleString('en-US', options);
    },

  }
}
</script>

<style>
/* Event Card Styles */
.event-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  display: flex;
  flex-direction: column;
}

h3 {
  font-size: 1.5rem;
  margin-bottom: 8px;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #0056b3;
}

/* Add any additional styles you need */
</style>
