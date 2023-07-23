<template>
  <div>
    <h1>Events Page</h1>
    <div v-if="Allevents.length > 0">
      <div v-for="event in Allevents" :key="event._id">
        <EventCard :event="event" @book-event="bookEvent" />
      </div>
    </div>
    <div v-else>
      <p>No events found.</p>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'; // Import mapState from Vuex
import EventCard from '@/components/EventCard.vue'; // Import the EventCard component

export default {
  components: {
    EventCard,
  },
  computed: {
    ...mapState(['Allevents']), // Map the 'events' state from the store to the component's computed properties
  },
  mounted() {
    // Dispatch an action to fetch events data from the backend using Vuex
    this.$store.dispatch('fetchEvents')
      .catch((error) => {
        console.error('Error fetching events:', error);
      });
  },
  methods: {
    ...mapActions(["bookevent"]), // Import the bookevent action
    bookEvent(event) {
      // Call the participateEventAPI function with the event ID
      this.participateEventAPI(event._id)
        .then(() => {
          // If booking is successful, trigger the bookevent action to update the events state
          this.bookevent();
        })
        .catch((error) => {
          // Handle any errors during booking
          console.error(error);
        });
    },
  }
};
</script>

<style>
/* Apply your custom CSS styles here */
</style>
