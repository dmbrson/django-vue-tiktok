<template>
  <header class="header">
    <div class="header__burger" @click="toggleMenu">
      <span class="burger-line"></span>
      <span class="burger-line"></span>
      <span class="burger-line"></span>
    </div>
    <div class="header__logo">
      <router-link to="/">
        <img :src="logoUrl" alt="Logo" class="logo" />
      </router-link>
    </div>
    <div class="header__search">
      <input type="text" placeholder="Search" />
      <button>Search</button>
    </div>
    <div class="header__nav">
      <ul>
        <li><router-link to="/registration">Registration</router-link></li>
        <li><router-link to="/profile">Profile</router-link></li>
        <li><router-link to="/login">Login</router-link></li>
      </ul>
    </div>
    <div class="side-menu" :class="{ open: isMenuOpen }">
      <div class="side-menu__content">
        <ul>
          <li><router-link to="/">Главная</router-link></li>
          <li><router-link to="/subscriptions">Подписки</router-link></li>
          <li><router-link to="/history">История</router-link></li>
          <li><router-link to="/your-videos">Ваши видео</router-link></li>
          <li><router-link to="/liked-videos">Понравившиеся</router-link></li>
        </ul>
      </div>
    </div>
    <div class="overlay" @click="toggleMenu" :class="{ active: isMenuOpen }"></div>
  </header>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Header',
  data() {
    return {
      logoUrl: 'http://localhost:8000/media/logos/your-logo.png',
      isMenuOpen: false
    }
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
      document.body.classList.toggle('menu-open', this.isMenuOpen);
    }
  }
}
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #ffffff;
  border-bottom: 1px solid #e5e5e5;
  position: relative;
  z-index: 1100;
}

.header__burger {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 25px;
  height: 25px;
  cursor: pointer;
  z-index: 1200;
  padding: 10px;
}

.burger-line {
  width: 100%;
  height: 3px;
  background-color: #333;
}

.header__logo .logo {
  height: 40px;
}

.header__search {
  display: flex;
  align-items: center;
  flex-grow: 1;
  margin: 0 20px;
}

.header__search input {
  width: 100%;
  padding: 10px;
  border: 1px solid #e5e5e5;
  border-radius: 20px 0 0 20px;
  outline: none;
}

.header__search button {
  padding: 10px 20px;
  border: 1px solid #e5e5e5;
  border-left: none;
  background-color: #efefef;
  border-radius: 0 20px 20px 0;
  cursor: pointer;
}

.header__nav ul {
  list-style: none;
  display: flex;
  align-items: center;
  margin: 0;
  padding: 0;
}

.header__nav li {
  margin-left: 20px;
}

.header__nav a {
  color: #333;
  text-decoration: none;
  font-weight: bold;
}

.side-menu {
  position: fixed;
  top: 0;
  left: 0;
  width: 250px;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transform: translateX(-100%);
  transition: transform 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  z-index: 1000;
}

.side-menu.open {
  transform: translateX(0);
}

.side-menu__content {
  background-color: #fff;
  width: 250px;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.side-menu ul {
  list-style: none;
  margin: 0;
  padding: 20px 0;
}

.side-menu li {
  padding: 10px 20px;
}

.side-menu a {
  color: #333;
  text-decoration: none;
  font-weight: bold;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0);
  transition: background-color 0.3s ease-in-out;
  z-index: 500; /* Changed to be below the header */
  pointer-events: none; /* Initially, the overlay does not block clicks */
}

.overlay.active {
  background-color: rgba(0, 0, 0, 0.5);
  pointer-events: auto; /* When active, the overlay blocks clicks */
}

body.menu-open {
  overflow: hidden;
}
</style>