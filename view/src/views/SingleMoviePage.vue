<template>
  <div v-if="singlemovie" class="single-movie-page">
    <div class="movie-details">
      <img :src="singlemovie.image" :alt="singlemovie.title" class="movie-image" />
      <div class="movie-info">
        <h2 class="movie-title">{{ singlemovie.title }}</h2>
        <p class="movie-description">{{ singlemovie.description }}</p>
       
        <h3>Show Timings</h3>
        <ul>
          <li v-for="show in shows" :key="show._id">
            {{ show.timing }}
            <button class="book-button" @click="bookShow(show._id)">Book Show</button>
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
   </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['singlemovie','shows']),
  },

  methods: {
   async bookShow(showId) {
       // Check if the user is logged in
       let isLoggedIn = false; // Replace this with your actual login check
       if (this.$store.state.user) {
       isLoggedIn=true
      }
if (isLoggedIn) {
  // User is logged in, show the booking form
  this.showBookingForm();
} else {
  // User is not logged in, show the login prompt
  this.showLoginPrompt();
}
},
showLoginPrompt() {
// Implement the logic to display the login prompt, e.g., a modal or a separate login page
alert('Please log in to book the movie.');
},
showBookingForm() {
// Implement the logic to display the booking form, e.g., a modal or a separate booking page
// Collect participant details from the user and call the backend API to create a participant
const participantDetails = {
  name: '',
  email: '',
  phoneno: '',
  address: '',
  events: [],
  quantity: 1,
  totalamount: this.singlemovie.ticketprice,
};

// Make a POST request to the backend to create the participant and associate it with the movie
// Replace 'api/participants' with your backend API endpoint for creating participants
fetch('/api/participants', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(participantDetails),
})
  .then((response) => response.json())
  .then((data) => {
    // Handle the response from the backend if needed
    console.log(data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });

    },
    submitParticipantForm(participantData) {
      // Call the backend API to create a participant and book the show
      const bookingData = {
        movieId: this.singlemovie._id,
        participant: participantData,
      };

      fetch("/api/book_show", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(bookingData),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Booking success:", data);
          // Handle success, show confirmation message or navigate to confirmation page
        })
        .catch((error) => {
          console.error("Error booking show:", error);
          // Handle error, show error message to the user
        });
    },
  },
  },
  created() {
    // Fetch the single movie data using the movie ID from the URL params
    const movieId = this.$route.params.id;
    // Dispatch an action to fetch the single movie data
    this.$store.dispatch('fetchSingleMovie', movieId);
    this.$store.dispatch('fetchMovieShows',movieId)
  },
};
</script>

<style>
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

.movie-image {
  max-width: 300px;
  max-height: 450px;
  border-radius: 5px;
  margin-right: 20px;
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
