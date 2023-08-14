<template>
  <div class="user-registration">
    <h2>User Registration</h2>
    <form @submit.prevent="registerUser">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="userData.username" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="userData.email" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="userData.password" required />
      </div>
      <div class="form-group">
        <label for="role">Role:</label>
        <input type="text" id="role" v-model="userData.role" disabled />
      </div>
      <div class="form-group">
        <label for="user_status">User Status:</label>
        <select id="user_status" v-model="userData.user_status">
          <option value="true">Active</option>
          <option value="false">Inactive</option>
        </select>
      </div>
      <div class="form-group">
        <label for="gender">Gender:</label>
        <select id="gender" v-model="userData.gender">
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
      </div>
      <div class="form-group">
        <label for="membership_type">Membership Type:</label>
        <input type="text" id="membership_type" v-model="userData.membership_type" disabled />
       
      </div>
      <div class="form-group">
        <label for="bio">Bio:</label>
        <textarea id="bio" v-model="userData.bio"></textarea>
      </div>
      <div class="form-group">
        <label for="date_of_birth">Date of Birth:</label>
        <input type="date" id="date_of_birth" v-model="userData.date_of_birth" />
      </div>
      <div class="form-group">
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="userData.location" />
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        email: '',
        password: '',
        role: 'user', // Default role is set to 'user'
        user_status: true,
        gender: 'Other',
        membership_type: 'general',
        bio: '',
        date_of_birth: '',
        location: '',
      },
      errorMessage: '',
    };
  },
  methods: {
    registerUser() {
      // Rest of the method remains the same
      // ...
     // const {userData} =this
      this.$store.dispatch('registerUser',{ userData: this.userData })
        .then(() => {
          console.log('User registered successfully!');
          this.userData = {
            username: '',
        email: '',
        password: '',
        role: 'user', // Default role is set to 'user'
        user_status: true,
        gender: 'Other',
        membership_type: 'general',
        bio: '',
        date_of_birth: '',
        location: '',
          };
          this.errorMessage = '';
        })
        .catch((error) => {
          console.error('Registration failed:', error.message);
          this.errorMessage = error.message;
        });
    },
  },
};
</script>

<style>
/* Your CSS styles here */

.user-registration {
  max-width: 400px;
  margin: 0 auto;
}

.user-registration h2 {
  margin-bottom: 20px;
}

.user-registration form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.user-registration label {
  font-weight: bold;
}

.user-registration input,
.user-registration textarea,
.user-registration select {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.user-registration button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.user-registration .error {
  color: red;
}
</style>



 