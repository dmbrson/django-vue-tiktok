<template>
  <nav>
    <ul>
      <li><router-link to="/">Главная</router-link></li>
      <li><router-link to="/subscriptions">Подписки</router-link></li>
      <li><router-link to="/history">История</router-link></li>
      <li><router-link to="/your-videos">Ваши видео</router-link></li>
      <li><router-link to="/liked-videos">Понравившиеся</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Navbar'
}
</script>

<style scoped>
nav {
  background-color: #333;
  padding: 1rem;
}
ul {
  list-style: none;
  display: flex;
  justify-content: space-around;
  margin: 0;
  padding: 0;
}
li {
  margin: 0;
}
a {
  color: white;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
</style>