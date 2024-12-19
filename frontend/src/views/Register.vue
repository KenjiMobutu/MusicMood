<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { AuthService } from '../services/auth.service'
import { GENRES } from '../config/constants'
import axios from 'axios';


const router = useRouter()
const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const favoriteGenres = ref<string[]>([])
const favoriteArtists = ref('')
const error = ref('')
const loading = ref(false)


// Obtenez le jeton CSRF depuis les cookies
function getCsrfToken() {
  const name = 'csrftoken';
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    const part = parts.pop();
    if (part) {
      const splitPart = part.split(';');
      if (splitPart.length > 0) {
        return splitPart.shift();
      }
    }
  }
  return null;
}

// Ajoutez le jeton CSRF dans les en-têtes d'Axios
axios.defaults.withCredentials = true;
axios.defaults.headers.common['X-CSRFToken'] = getCsrfToken() || '';
async function handleSubmit() {
  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match'
    return
  }
  axios.defaults.headers.common['X-CSRFToken'] = getCsrfToken() || '';
  loading.value = true
  error.value = ''

  try {
    await AuthService.getInstance().register({
      username: username.value,
      email: email.value,
      password: password.value,
      favorite_genres: favoriteGenres.value,
      favorite_artists: favoriteArtists.value.split(',').map(a => a.trim())
    })
    router.push('/')
  } catch (e) {
    error.value = 'Registration failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-white p-8 rounded-lg shadow">
      <div>
        <h2 class="text-center text-3xl font-extrabold text-gray-900">
          Create your account
        </h2>
      </div>

      <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">

        <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
          {{ error }}
        </div>

        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
            <input
              id="username"
              v-model="username"
              type="text"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            >
          </div>

          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input
              id="email"
              v-model="email"
              type="email"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            >
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input
              id="password"
              v-model="password"
              type="password"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            >
          </div>

          <div>
            <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirm Password</label>
            <input
              id="confirm-password"
              v-model="confirmPassword"
              type="password"
              required
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            >
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700">Favorite Genres</label>
            <div class="mt-2 space-y-2">
              <div v-for="genre in GENRES" :key="genre" class="flex items-center">
                <input
                  :id="genre"
                  v-model="favoriteGenres"
                  type="checkbox"
                  :value="genre"
                  class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                >
                <label :for="genre" class="ml-2 text-sm text-gray-700">{{ genre }}</label>
              </div>
            </div>
          </div>

          <div>
            <label for="favorite-artists" class="block text-sm font-medium text-gray-700">
              Favorite Artists (comma-separated)
            </label>
            <input
              id="favorite-artists"
              v-model="favoriteArtists"
              type="text"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
              placeholder="e.g. Artist1, Artist2, Artist3"
            >
          </div>
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
        >
          {{ loading ? 'Creating account...' : 'Create account' }}
        </button>

        <div class="text-center">
          <router-link to="/login" class="text-indigo-600 hover:text-indigo-500">
            Already have an account? Sign in
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>
