<template>
  <div id="app">
    <Header />
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Header,
    Navbar
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  text-align: center;
}

nav {
  margin-top: 10px;
}
</style>