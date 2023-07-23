<!-- src/components/Navbar.vue -->
<template>
  <nav>
    <ul>
      <li @click="navigateTo('/')">Home</li>
      <li @click="navigateTo('/events')">Events</li>
      <li @click="navigateTo('/bookings')">Bookings</li>
      <li @click="navigateTo('/login')">Login</li>
      <li @click="navigateTo('/create-event')" v-if="isAdmin" >Create Event</li>
      <!-- Add more navigation items for other pages as needed -->
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavbarMenu',
  computed: {
    isAdmin() {
      // Access the isAdmin property from the Vuex store state
      const user = this.$store.state.user;
      // Check if the user is logged in and has the "role" key equal to "admin"
     
      return user && user.user_data.role === 'admin';
    },
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    },
  },
};
</script>

<style>
nav {
  background-color: #333;
  padding: 10px;
}

ul {
  list-style: none;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding: 0;
}

li {
  margin: 0 10px;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
  text-transform: uppercase;
}

li:hover {
  color: #ff6600;
}
</style>
