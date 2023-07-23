<!-- src/components/LoginForm.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div>
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
     New User? <router-link :to="'/register'">Create an Account</router-link>
  </template>
<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      const { username, password } = this;
      this.$store.dispatch('login', { username, password })
        .then(() => {
          console.log('Logged in successfully!');
          if (this.$route.meta.fromHistory) {
            // Redirect to the previous page in the browser history
            this.$router.go(-1);
          } else {
            // Otherwise, redirect to the dashboard page
            this.$router.push('/');
          }   
        })
        .catch((error) => {
          console.error('Login failed:', error.message);
        });
    },
  },
};
</script>