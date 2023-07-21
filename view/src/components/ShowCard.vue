<!-- ShowCard.vue -->
<template>
    <div class="show-card">
      <h3>{{ show.name }}</h3>
      <p>{{ show.timing }}</p>
      <!-- Add more show details here -->
      <button @click="onBookShow">Book Now</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      show: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onBookShow() {
        // Handle booking the show here
        // You can use Vuex actions or emit an event to the parent component
        // to trigger the booking process
      },
    },
  };
  </script>
  
  <style>
  /* Add your show card CSS styles here */
  </style>
  