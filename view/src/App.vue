<!-- src/App.vue -->
<template>
  <div id="app">
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/NavbarMenu.vue';

export default {
  components: {
    Navbar,
  },
};
</script>
