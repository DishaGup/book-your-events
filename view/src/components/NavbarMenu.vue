<!-- src/components/Navbar.vue -->
<template>
  <header class="header" data-header>
    <div class="container">

      <div class="overlay" data-overlay></div>

      <a href="./index.html" class="logo">
        <img src="../assets/logo.png" alt="movieflix logo"/>
      </a>

      <div class="header-actions">

        <button class="search-btn">
          <ion-icon name="search-outline"></ion-icon>
        </button>

        <div class="lang-wrapper">
          <label for="language">
            <ion-icon name="globe-outline"></ion-icon>
          </label>

          <select name="language" id="language">
            <option value="en">EN</option>
            <option value="au">AU</option>
            <option value="ar">AR</option>
            <option value="tu">TU</option>
          </select>
        </div>

        <button @click="navigateTo('/login')" class="btn btn-primary">Login in</button>

      </div>

      <button class="menu-open-btn" data-menu-open-btn>
        <ion-icon name="reorder-two"></ion-icon>
      </button>
      <nav class="navbar" data-navbar>

        <div class="navbar-top">

          <a href="/" class="logo">
            <img src="../assets/logo.png" alt="movieflix logo"/>
          </a>

          <button class="menu-close-btn" data-menu-close-btn>
            <ion-icon name="close-outline"></ion-icon>
          </button>

        </div>

        <ul class="navbar-list">

          <li>
            <a href="/" class="navbar-link">Home</a>
          </li>

          <li>
            <a href="/movies" class="navbar-link">Movie</a>
          </li>

          <li>
            <a href="/events" class="navbar-link">Events</a>
          </li>

          <li>
            <a href="/bookings" class="navbar-link">Bookings</a>
          </li>

          <li>
            <a href="/create-event" class="navbar-link">Create Events</a>
          </li>

        </ul>

        <ul class="navbar-social-list">

          <li>
            <a href="#" class="navbar-social-link">
              <ion-icon name="logo-twitter"></ion-icon>
            </a>
          </li>

          <li>
            <a href="#" class="navbar-social-link">
              <ion-icon name="logo-facebook"></ion-icon>
            </a>
          </li>

          <li>
            <a href="#" class="navbar-social-link">
              <ion-icon name="logo-pinterest"></ion-icon>
            </a>
          </li>

          <li>
            <a href="#" class="navbar-social-link">
              <ion-icon name="logo-instagram"></ion-icon>
            </a>
          </li>

          <li>
            <a href="#" class="navbar-social-link">
              <ion-icon name="logo-youtube"></ion-icon>
            </a>
          </li>

        </ul>

      </nav>

    </div>
  </header>
</template>




<script>
export default {
  name: 'NavbarMenu',
  computed: {
    isAdmin() {
      // Access the isAdmin property from the Vuex store state
      const user = this.$store.state.user;
      // Check if the user is logged in and has the "role" key equal to "admin"
      console.log(user)
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

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding-block: 25px;
  transition: var(--transition-2);
  z-index: 4;
}

.header.active {
  background: var(--eerie-black);
  padding-block: 20px;
}

.header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-actions {
  display: none;
}

.menu-open-btn {
  color: var(--white);
  font-size: 40px;
}

.navbar {
  position: fixed;
  top: 0;
  right: -300px;
  background: var(--eerie-black);
  width: 100%;
  max-width: 300px;
  height: 100%;
  box-shadow: -1px 0 3px hsl(0, 0%, 0%, 0.2);
  transition: 0.15s ease-in;
  visibility: hidden;
  z-index: 3;
}

.navbar.active {
  right: 0;
  visibility: visible;
  transition: 0.25s ease-out;
}

.navbar-top {
  padding: 30px 25px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.menu-close-btn {
  color: var(--white);
  font-size: 25px;
  padding: 5px;
}

.menu-close-btn ion-icon {
  --ionicon-stroke-width: 80px;
}

.navbar-list {
  border-top: 1px solid hsla(0, 0%, 100%, 0.1);
  margin-bottom: 30px;
}

.navbar-link {
  color: var(--white);
  font-size: var(--fs-8);
  font-weight: var(--fw-500);
  padding: 10px 25px;
  border-bottom: 1px solid hsla(0, 0%, 100%, 0.1);
  transition: var(--transition-1);
}

.navbar-link:is(:hover, :focus) {
  color: var(--citrine);
}

.navbar-social-list {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.navbar-social-link {
  font-size: 20px;
  color: var(--white);
  transition: var(--transition-1);
}

.navbar-social-link:is(:hover, :focus) {
  color: var(--citrine);
}

.overlay {
  position: fixed;
  inset: 0;
  background: hsla(204, 18%, 11%, 0.8);
  opacity: 0;
  pointer-events: none;
  z-index: 1;
  transition: var(--transition-2);
}

.overlay.active {
  opacity: 1;
  pointer-events: all;
}</style>
