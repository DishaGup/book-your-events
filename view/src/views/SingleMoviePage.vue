<template>
  <div v-if="singlemovie" class="single-movie-page">

    <div :style="backgroundStyle" class="movie-background">
    <div class="movie-image-container">
      <img :src="singlemovie.image" :alt="singlemovie.title" class="movie-image" />
    </div>

   </div>




    <div class="movie-details">
          <div class="movie-info">
        <h2 class="movie-title">{{ singlemovie.title }}</h2>
        <p class="movie-description">{{ singlemovie.description }}</p>

        <h3>Show Timings</h3>
        <ul>
          <li v-for="show in shows" :key="show._id">
            {{ show.timing }}
          </li>
        </ul>

        <p><strong>Genre:</strong> {{ singlemovie.genre }}</p>
        <p><strong>Duration:</strong> {{ singlemovie.duration }} hours</p>
        <p><strong>Cast:</strong></p>
        <ul class="cast-list">
          <li v-for="castMember in singlemovie.cast" :key="castMember">{{ castMember }}</li>
        </ul>
        <p><strong>Movie Date:</strong> {{ singlemovie.movieDate }}</p>
        <p><strong>Rating:</strong> {{ singlemovie.rating }}</p>
        <!-- Add other movie details here -->
      </div>
    </div>
    <div v-if="user && user.user_data.role === 'admin'">
      <h3>Add Show Timings</h3>
      <form @submit.prevent="addShowTimings">
        <label>Location</label>
        <select v-model="location">
        <option value="">Choose Location</option>
        <option value="Agra">Agra</option>
        <option value="Mumbai">Mumbai</option>
        <option value="Delhi">Delhi</option>
        <option value="Chandigarh">Chandigarh</option>

      </select>
        <div v-for="(timing, index) in newShowTimings" :key="index">
          <input type="text" v-model="timing.startTime" placeholder="Start Time (e.g., 6:00 PM)" required />
          <input type="text" v-model="timing.endTime" placeholder="End Time (e.g., 8:00 PM)" required />
          <button type="button" @click="removeTiming(index)">Remove</button>
        </div>
        <button type="submit">Add timing</button>
      </form>
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState(['singlemovie', 'shows', 'user',]),
    backgroundStyle() {
    if (this.singlemovie && this.singlemovie.image) {
      return {
        backgroundImage: `url(${this.singlemovie.image})`,
      };
    } else {
      return {
        backgroundImage: `url(https://media.tenor.com/qEl3jTTMQcAAAAAM/red.gif)`,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
      };
    }
  },
  },
  data() {
    return {
      newShowTimings: [],
      location:''
    };
  },
  methods: {
    ...mapActions(['addShowTimingAction', 'removeShowTiming', 'fetchSingleMovie', 'fetchMovieShows']),

    addTiming() {
      this.addShowTimingForm({ startTime: '', endTime: '' });
    },

    removeTiming(index) {
      this.removeShowTiming(index);
    },

    async addShowTimings() {
      if (this.newShowTimings.some(timing => !timing.startTime || !timing.endTime)) {
        alert("Please fill all show timings.");
        return;
      }

      const timingsData = this.newShowTimings.map(({ startTime, endTime }) => ({
        startTime,
        endTime,
      }));

      try {

      let data={
        timings:timingsData,location:this.location
      }
        await this.addShowTimingAction({ movieId: this.singlemovie._id, data });

        this.newShowTimings = [];
        this.fetchMovieShows(this.singlemovie._id);
      } catch (error) {
        console.error('Error adding show timings:', error);
      }
    },
  },
  created() {
    const movieId = this.$route.params.id;
    this.$store.dispatch('fetchSingleMovie', movieId);
    this.$store.dispatch('fetchMovieShows', movieId);

    this.newShowTimings = [
      { startTime: '9:00 AM', endTime: '11:00 AM' },
      { startTime: '1:00 PM', endTime: '3:00 PM' },
    ];

  },
};
</script>

<style scoped>
/* Your movie details and styles */
.single-movie-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.movie-details {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
.movie-background {
  position: relative;
  height: 5cm;
  /* Set the background image URL here */
 
  /* Add backdrop effect */
  background-color: rgba(0, 0, 0, 0.5);
}

.movie-image-container {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3cm;
  border-radius: 10px;
  width: 300px;
  /* Add padding or margin here if needed */
}

.movie-image {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  /* Add additional styles for the movie image if needed */
}

.movie-info {
  display: flex;
  flex-direction: column;
}

.movie-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.movie-description {
  margin-bottom: 15px;
}

.cast-list {
  margin-top: 0;
  padding-left: 20px;
}

.cast-list li {
  margin-bottom: 5px;
}

.book-button {
  padding: 10px 20px;
  font-size: 18px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.book-button:hover {
  background-color: #0056b3;
}
</style>
