<template>
    <div class="participant-form-overlay">
      <div class="participant-form-container">
        <h2>Participant Details</h2>
        <form @submit.prevent="submitForm">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="participant.name" required />
  
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="participant.email" />
  
          <label for="phoneno">Phone Number:</label>
          <input type="text" id="phoneno" v-model="participant.phoneno" />
  
          <label for="address">Address:</label>
          <textarea id="address" v-model="participant.address"></textarea>
  
          <button type="submit">Book Event</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        participant: {
          name: "",
          email: "",
          phoneno: "",
          address: "",
        },
      };
    },
    methods: {
      submitForm() {
        this.$emit("book-event", this.participant);
      },
    },
  };
  </script>
  
  <style>
  .participant-form-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .participant-form-container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  input,
  textarea {
    margin-bottom: 16px;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  