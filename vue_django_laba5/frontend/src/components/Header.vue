<template>
  <header class="header">
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
  </header>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Header',
   data() {
    return {
      logoUrl: 'http://localhost:8000/media/logos/your-logo.png'
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
</style>