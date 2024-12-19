<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { AuthService } from '../services/auth.service'
import type { User } from '../types/user'
import type { RecommendationResponse } from '../types/music'

const user = ref<User | null>(null)
const history = ref<RecommendationResponse[]>([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const auth = AuthService.getInstance()
    user.value = auth.getState().user

    const response = await fetch('http://localhost:8000/api/recommendations/history', {
      headers: {
        'Authorization': `Bearer ${auth.getState().token}`
      }
    })

    if (!response.ok) throw new Error('Failed to fetch history')
    history.value = await response.json()
  } catch (e) {
    error.value = 'Failed to load profile data'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="max-w-4xl mx-auto p-6">
    <div v-if="loading" class="text-center py-4">
      <p class="text-gray-600">Loading profile...</p>
    </div>

    <div v-else-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
      {{ error }}
    </div>

    <template v-else>
      <div class="bg-white rounded-lg shadow-md p-6 mb-6">
        <h2 class="text-2xl font-semibold mb-4">Profile</h2>
        
        <div class="space-y-4">
          <div>
            <p class="text-sm text-gray-500">Username</p>
            <p class="text-lg">{{ user?.username }}</p>
          </div>
          
          <div>
            <p class="text-sm text-gray-500">Email</p>
            <p class="text-lg">{{ user?.email }}</p>
          </div>
          
          <div>
            <p class="text-sm text-gray-500">Favorite Genres</p>
            <div class="flex flex-wrap gap-2 mt-1">
              <span
                v-for="genre in user?.favorite_genres"
                :key="genre"
                class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full text-sm"
              >
                {{ genre }}
              </span>
            </div>
          </div>
          
          <div>
            <p class="text-sm text-gray-500">Favorite Artists</p>
            <div class="flex flex-wrap gap-2 mt-1">
              <span
                v-for="artist in user?.favorite_artists"
                :key="artist"
                class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full text-sm"
              >
                {{ artist }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white rounded-lg shadow-md p-6">
        <h3 class="text-xl font-semibold mb-4">Recommendation History</h3>
        
        <div v-if="history.length === 0" class="text-center py-4 text-gray-500">
          No recommendations yet
        </div>
        
        <div v-else class="space-y-6">
          <div
            v-for="recommendation in history"
            :key="recommendation.id"
            class="border-b border-gray-200 pb-4 last:border-0"
          >
            <div class="mb-2">
              <span class="text-sm text-gray-500">
                {{ new Date(recommendation.created_at).toLocaleDateString() }}
              </span>
            </div>
            
            <div class="mb-2">
              <span class="text-sm font-medium">Preferences:</span>
              <span class="ml-2 text-sm text-gray-600">
                {{ recommendation.preferences.genre }} music from the {{ recommendation.preferences.decade }}
                ({{ recommendation.preferences.language }}, {{ recommendation.preferences.mood }})
              </span>
            </div>
            
            <ul class="space-y-1">
              <li
                v-for="(song, index) in recommendation.songs"
                :key="index"
                class="text-gray-700"
              >
                {{ song }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>