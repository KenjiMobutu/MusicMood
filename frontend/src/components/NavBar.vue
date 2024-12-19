<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { AuthService } from '../services/auth.service'

const router = useRouter()
const auth = AuthService.getInstance()
const isAuthenticated = computed(() => auth.getState().isAuthenticated)
const user = computed(() => auth.getState().user)

function handleLogout() {
  auth.logout()
  router.push('/login')
}
</script>

<template>
  <nav class="bg-white shadow-lg">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="text-2xl font-bold text-indigo-600">
            MusicMatch
          </router-link>
        </div>
        
        <div class="flex items-center space-x-4">
          <template v-if="isAuthenticated">
            <router-link
              to="/profile"
              class="text-gray-700 hover:text-indigo-600"
            >
              {{ user?.username }}'s Profile
            </router-link>
            <button
              @click="handleLogout"
              class="text-gray-700 hover:text-indigo-600"
            >
              Logout
            </button>
          </template>
          <template v-else>
            <router-link
              to="/login"
              class="text-gray-700 hover:text-indigo-600"
            >
              Login
            </router-link>
            <router-link
              to="/register"
              class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"
            >
              Register
            </router-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>