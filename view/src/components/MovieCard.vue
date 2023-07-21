<!-- MovieCard.vue -->
<template>
    <div class="movie-card">
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.genre }}</p>
      <!-- Add more movie details here -->
      <button @click="onBookMovie">Book Now</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      movie: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onBookMovie() {
        // Handle booking the movie here
        // You can use Vuex actions or emit an event to the parent component
        // to trigger the booking process
      },
    },
  };
  </script>
  
  <style>
  /* Add your movie card CSS styles here */
  </style>
  