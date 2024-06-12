<template>
  <div class="home">
    <h1>Welcome to My Website!</h1>
    <ul>
      <li><router-link to="/registration">Registration</router-link></li>
      <li><router-link to="/profile">Profile</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Home',
}
</script>

<style scoped>
h1 {
  margin-bottom: 20px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin-bottom: 10px;
}
a {
  color: #42b983;
  text-decoration: none;
}
</style>