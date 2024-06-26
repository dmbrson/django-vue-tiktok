<template>
  <div class="register">
    <h1>Register Page</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Register',
  data() {
    return {
      username: '',
      password: '',
      email: '',
      error: null,
      message: null,
    }
  },
  methods: {
    async register() {
      try {
        const response = await fetch('http://localhost:8000/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
            email: this.email,
          }),
        });

        const data = await response.json();

        if (!response.ok) {
          this.error = data.error;
          this.message = null;
        } else {
          this.message = data.message;
          this.error = null;
        }
      } catch (err) {
        this.error = 'Something went wrong';
        this.message = null;
      }
    },
  },
}
</script>

<style scoped>
/* ваши стили */
</style>