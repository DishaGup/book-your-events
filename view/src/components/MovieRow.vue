<template>
  <div class="movie-row">
    <h2>{{ title }}</h2>
    <div class="movie-cards">
      <MovieCard v-for="movie in movies" :key="movie._id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieCard from './MovieCard.vue';


export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    movies:{
      type:Array
    }
  },
  components: {
    MovieCard,
  },
  // computed: {
  //   ...mapState(['Allmovies']),
  // },
  created() {
    console.log('Movierow props:', this.title);
  },
};
</script>

<style>
/* Add your movie row CSS styles here */
.movie-row {
  margin-bottom: 30px;
}

.movie-row h2 {
  font-size: 24px;
  font-weight: bold;
  margin-left: 20px;
}

.movie-cards {
  display: flex;
  overflow-x: auto;
  gap: 10px;
  padding: 10px 20px;
  margin-top: 10px;
}

/* Scrollbar styling for the movie cards */
.movie-cards::-webkit-scrollbar {
  height: 8px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.movie-cards::-webkit-scrollbar-thumb {
  background-color: #aaa;
  border-radius: 5px;
}

.movie-cards::-webkit-scrollbar-thumb:hover {
  background-color: #888;
}
</style>
