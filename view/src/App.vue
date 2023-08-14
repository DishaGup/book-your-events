<!-- src/App.vue -->
<template>
  <body id="app">
  
<Navbar />
<router-view></router-view>

  </body>
</template>

<script>
import Navbar from './components/NavbarMenu.vue';

export default {
  components: {
    Navbar,
  },
};
</script>

<style scoped>

body { background: var(--eerie-black); }

body.active { overflow: hidden; }

</style>