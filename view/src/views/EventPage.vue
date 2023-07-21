<!-- EventsPage.vue -->
<template>
  <div>
    <h1>Events Page</h1>
    <div v-if="events.length > 0">
      <div v-for="event in events" :key="event._id">
        <EventCard :event="event" />
      </div>
    </div>
    <div v-else>
      <p>No events found.</p>
    </div>
  </div>
</template>

<script>
import EventCard from '@/components/EventCard.vue'; // Import the EventCard component

export default {
  components: {
    EventCard,
  },
  data() {
    return {
      events: [], // Store the events data fetched from the backend
    };
  },
  mounted() {
    // Fetch events data from the backend using API calls (e.g., Axios)
    // and update the events array
  },
};
</script>
