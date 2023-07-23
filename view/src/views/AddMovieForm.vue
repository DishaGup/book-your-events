<template>

<div class="container">
      <h2>Add Movie</h2>
      <form @submit.prevent="addMovie">
        <label for="title">Title *</label>
        <input type="text" id="title" v-model="title" required>

        <label for="rating">Rating</label>
        <input type="number" id="rating" v-model="rating" step="0.1">

        <label for="description">Description *</label>
        <textarea id="description" v-model="description" required></textarea>

        <label for="image">Image *</label>
        <textarea id="image" v-model="image" required></textarea>

        <label for="genre">Genre</label>
        <input type="text" id="genre" v-model="genre">

        <label for="duration">Duration</label>
        <input type="text" id="duration" v-model="duration">

        <label for="cast">Cast</label>
        <textarea id="cast" v-model="cast"></textarea>

        <label for="movieDate">Release Date</label>
        <input type="date" id="movieDate" v-model="movieDate">

        <button type="submit">Add Movie</button>
      </form>
    </div>
  
</template>


<script>

export default{
    data() {
    return {
      title: '',
      rating: null,
      description: '',
      genre: '',
      duration: '',
      cast: '',
      movieDate: '',
      image:'',
    };
  },
  methods: {
    addMovie() {
      const movieData = {
        title: this.title,
        rating: this.rating,
        description: this.description,
        genre: this.genre,
        duration: this.duration,
        cast: this.cast.split('\n').map(name => name.trim()), // Convert cast to an array of names
        movieDate: this.movieDate,
        image :this.image
      };
      this.$store.dispatch('createMovie', { movieData})
        .then(() => {
         alert("movie created")
        }).catch(() => alert("movie not created, try sometime"))
      // After creating the event, you can show a success message or redirect the user.
    
      // Send the movieData to the backend using an HTTP request
      // Example using Axios: (remember to include Axios in your project)
      // axios.post('/api/movies', movieData)
      //   .then(response => {
      //     console.log('Movie added successfully!');
      //   })
      //   .catch(error => {
      //     console.error('Failed to add movie:', error);
      //   });

      // For this example, we will just log the movieData to the console
      console.log(movieData);
    }


  }}
</script>


<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 500px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    font-weight: bold;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
textarea {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 10
}


</style>