<template>
  <div>
    <!-- Your Create Event form here -->
    <form @submit.prevent="createEvent">

      <input type="text" v-model="eventName" placeholder="Event Name" />
      <input type="datetime-local" v-model="eventDate" placeholder="Event Date" />
      <input type="number" v-model="ticketPrice" placeholder="Ticket Price" />
      <input type="text" v-model="venue" placeholder="Venue" />
      <select v-model="location">
        <option value="">Select City</option>
        <option value="Agra">Agra</option>
        <option value="Delhi">Delhi</option>
        <option value="Noida">Noida</option>
        <option value="Jaipur">Jaipur</option>

      </select>
      <select v-model="category">
        <option value="">Choose event category</option>
        <option value="Stand Up">Stand Up</option>
        <option value="Poetry">Poetry</option>
        <option value="Music">Music</option>
        <option value="Game">Game</option>

      </select>
      <textarea v-model="description" placeholder="Description"></textarea>

      <button type="submit">Create Event</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreateEvent',
  data() {
    return {
      eventName: '',
      eventDate: '',
      ticketPrice: null,
      venue: '',
      description: '',
      location: "",
      category: "",
    };
  },
  methods: {
    createEvent() {
      const eventData = {
        eventName: this.eventName,
        eventDate: new Date(this.eventDate).toISOString(),
        ticket_price: this.ticketPrice,
        venue: this.venue,
        description: this.description,
        location: this.location,
        category: this.category,
       
      };
      const token = this.$store.state.user.token;

      if (!token) {
        console.error('Token is missing!');
        return;
      }

      const config = {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };
      this.$store.dispatch('createEvent', { eventData, config })
        .then(() => {
         alert("event created")
        }).catch(() => alert("event not created, try sometime"))
      // After creating the event, you can show a success message or redirect the user.
    },
  },
};
</script>


