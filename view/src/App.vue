<template>
  <div id="app">
    <UserRegistration />
  </div>
</template>

<script>
import UserRegistration from './components/UserRegistration.vue';

export default {
  components: {
    UserRegistration,
  },
};
</script>

<style>
#app {
  padding: 20px;
}
</style>
