import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Registration from '../views/Registration.vue'
import Profile from '../views/Profile.vue'
import Login from '../views/Login.vue'
import Subscriptions from '../views/Subscriptions.vue'
import History from '../views/History.vue'
import YourVideos from '../views/YourVideos.vue'
import LikedVideos from '../views/LikedVideos.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/subscriptions',
    name: 'Subscriptions',
    component: Subscriptions
  },
  {
    path: '/history',
    name: 'History',
    component: History
  },
  {
    path: '/your-videos',
    name: 'YourVideos',
    component: YourVideos
  },
  {
    path: '/liked-videos',
    name: 'LikedVideos',
    component: LikedVideos
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router