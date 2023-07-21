<!-- src/views/MoviesPage.vue -->
<template>
    <div>
      <h1>Movies Page</h1>
      <div v-if="movies.length > 0">
        <div v-for="movie in movies" :key="movie._id">
          <MovieCard :movie="movie" />
        </div>
      </div>
      <div v-else>
        <p>No movies found.</p>
      </div>
    </div>
  </template>
  
  <script>
  import MovieCard from '@/components/MovieCard.vue';
  
  export default {
    components: {
      MovieCard,
    },
    data() {
      return {
        movies: [], // Store the movies data fetched from the backend
      };
    },
    mounted() {
      // Fetch movies data from the backend using API calls (e.g., Axios)
      // and update the movies array
    },
  };
  </script>
  