<!-- src/views/CreateEventPage.vue -->
<template>
    <div class="create-event">
      <h2>Create Event</h2>
      <form @submit.prevent="handleSubmit">
        <label for="name">Event Name:</label>
        <input type="text" id="name" v-model="eventName" required>
        <label for="date">Event Date:</label>
        <input type="date" id="date" v-model="eventDate" required>
        <!-- Add other form fields for event details, such as ticket price, venue, description, etc. -->
        <button type="submit" v-if="isAdmin">Create Event</button>
        <span v-else>You need admin privileges to create an event.</span>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        eventName: '',
        eventDate: '',
        isAdmin: false, // Set to true if the user is an admin, otherwise, set to false
      };
    },
    created() {
      // Check if the user is logged in and has admin role
      this.checkAdminRole();
    },
    methods: {
      async checkAdminRole() {
        try {
          const response = await axios.get('/users/current');
          // Set isAdmin to true if the user has admin role
          this.isAdmin = response.data.role === 'admin';
        } catch (error) {
          console.error('Error checking admin role:', error);
        }
      },
      async handleSubmit() {
        if (this.isAdmin) {
          try {
            const eventData = {
              name: this.eventName,
              date: this.eventDate,
              // Add other event details here
            };
            // Make the API call to create the event
            const response = await axios.post('/events', eventData);
            // Handle the successful response here (e.g., show a success message)
            console.log('Event created:', response.data);
            // Optionally, you can navigate to the events page after creating the event
            this.$router.push('/events');
          } catch (error) {
            // Handle any errors that occurred during the API call
            console.error('Error creating event:', error);
          }
        } else {
          // Redirect the user to the login page if they are not logged in or not an admin
          this.$router.push('/login');
        }
      },
    },
  };
  </script>
   
  <style>
  .create-event {
    max-width: 400px;
    margin: 0 auto;
  }
  
  h2 {
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    padding: 10px;
    margin-bottom: 10px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  
  span {
    color: red;
  }
  </style>
  