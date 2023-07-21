<!-- BookingPage.vue -->
<template>
  <div>
    <h1>Booking Page</h1>
    <div v-if="bookings.length > 0">
      <div v-for="booking in bookings" :key="booking._id">
        <!-- Display booking details here (e.g., event, show, participant info) -->
      </div>
    </div>
    <div v-else>
      <p>No bookings found.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookings: [], // Store the bookings data fetched from the backend
    };
  },
  mounted() {
    // Fetch bookings data from the backend using API calls (e.g., Axios)
    // and update the bookings array
  },
};
</script>
