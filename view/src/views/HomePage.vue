<!-- src/views/HomePage.vue -->
<template>
  <div>
    <h1>Home Page</h1>
    <div v-if="movies.length > 0">
      <div v-for="movie in movies" :key="movie._id">
        <MovieCard :movie="movie" />
      </div>
    </div>
    <div v-else>
      <p>No movies found.</p>
    </div>

    <div v-if="shows.length > 0">
      <div v-for="show in shows" :key="show._id">
        <ShowCard :show="show" />
      </div>
    </div>
    <div v-else>
      <p>No shows found.</p>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue';
import ShowCard from '@/components/ShowCard.vue';

export default {
  components: {
    MovieCard,
    ShowCard,
  },
  data() {
    return {
      movies: [], // Store the movies data fetched from the backend
      shows: [], // Store the shows data fetched from the backend
    };
  },
  mounted() {
    // Fetch movies and shows data from the backend using API calls (e.g., Axios)
    // and update the movies and shows arrays
  },
};
</script>
