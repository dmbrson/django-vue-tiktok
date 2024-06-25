<template>
  <div id="app">
    <Navbar />
    <Header />

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
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>