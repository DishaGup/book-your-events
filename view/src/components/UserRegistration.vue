<template>
    <div class="user-registration">
      <h2>User Registration</h2>
      <form @submit.prevent="registerUser">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="userData.username" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="userData.email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="userData.password" required />
        </div>
        <div>
          <label for="role">Role:</label>
          <input type="text" id="role" v-model="userData.role"  />
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
          role: '',
        },
        errorMessage: '',
      };
    },
    methods: {
      async registerUser() {
        try {
          const response = await fetch('http://localhost:5050/api/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.userData),
          });
  
          if (response.ok) {
            alert('User registered successfully!');
            this.userData = {
              username: '',
              email: '',
              password: '',
              role: '',
            };
            this.errorMessage = '';
          } else {
            const data = await response.json();
            this.errorMessage = data.message || 'Failed to register user.';
          }
        } catch (error) {
          console.error('Error registering user:', error);
          this.errorMessage = 'An error occurred while registering the user.';
        }
      },
    },
  };
  </script>
  
  <style>
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
  
  .user-registration input {
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
  