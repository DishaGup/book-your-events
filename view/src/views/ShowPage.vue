<!-- src/views/ShowsPage.vue -->
<template>
    <div>
      <h1>Shows Page</h1>
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
  import ShowCard from '@/components/ShowCard.vue';
  
  export default {
    components: {
      ShowCard,
    },
    data() {
      return {
        shows: [], // Store the shows data fetched from the backend
      };
    },
    mounted() {
      // Fetch shows data from the backend using API calls (e.g., Axios)
      // and update the shows array
    },
  };
  </script>
  