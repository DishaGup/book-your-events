<!-- EventCard.vue -->
<template>
    <div class="event-card">
      <h3>{{ event.name }}</h3>
      <p>{{ event.date }}</p>
      <!-- Add more event details here -->
      <button @click="onBookEvent">Book Now</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      event: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onBookEvent() {
        // Handle booking the event here
        // You can use Vuex actions or emit an event to the parent component
        // to trigger the booking process
      },
    },
  };
  </script>
  
  <style>
  /* Add your event card CSS styles here */
  </style>
  