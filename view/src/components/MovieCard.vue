<template>
  <router-link :to="'/movie/' + movie._id" class="movie-card">
    <div class="movie-card-content">
      <div class="movie-card-header">
        <h3 class="movie-title">{{ movie.title }}</h3>
        <span class="movie-genre">{{ movie.genre }}</span>
      </div>
      <div class="movie-card-body">
        <img :src="movie.image" alt="Movie" class="movie-image" />
        <div class="movie-details">
          <p><strong>Rating:</strong> {{ movie.rating }}</p>
          <p><strong>Duration:</strong> {{ movie.duration }} hours</p>
          <p><strong>Cast:</strong> {{ movie.cast.join(", ") }}</p>
          <p><strong>Release Date:</strong> {{ movie.movieDate }}</p>
        </div>
      </div>
      <button class="book-button" @click="onBookMovie">Book Now</button>
    </div>
  </router-link>
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
.movie-card {
  display: block;
  text-decoration: none;
}

.movie-card-content {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  background-color: #fff;
  transition: box-shadow 0.2s ease;
}

.movie-card-content:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.movie-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.movie-title {
  font-size: 18px;
  font-weight: bold;
  margin: 0;
}

.movie-genre {
  font-size: 14px;
  color: #666;
}

.movie-card-body {
  display: flex;
  align-items: center;
}

.movie-image {
  width: 100px;
  height: 150px;
  object-fit: cover;
  border-radius: 4px;
  margin-right: 16px;
}

.movie-details {
  font-size: 14px;
  line-height: 1.6;
  color: #333;
}

.book-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.book-button:hover {
  background-color: #0056b3;
}
</style>
