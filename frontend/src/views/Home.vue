<script setup lang="ts">
import { ref } from 'vue'
import MusicForm from '../components/MusicForm.vue'
import RecommendationList from '../components/RecommendationList.vue'
import { AIService } from '../services/ai.service'
import type { MusicPreferences } from '../types/music'

const recommendations = ref<string[]>([])
const loading = ref(false)
const error = ref<string | null>(null)

async function handleSubmit(preferences: MusicPreferences) {
  loading.value = true
  error.value = null
  
  try {
    const aiService = AIService.getInstance()
    const result = await aiService.getRecommendations(preferences)
    
    if (result.error) {
      error.value = result.error
    } else {
      recommendations.value = result.songs
    }
  } catch (e) {
    error.value = 'An unexpected error occurred. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="max-w-4xl mx-auto p-6">
    <MusicForm @submit="handleSubmit" />
    
    <div v-if="loading" class="text-center py-4">
      <p class="text-gray-600">Getting recommendations...</p>
    </div>
    
    <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded mb-6">
      {{ error }}
    </div>
    
    <RecommendationList :songs="recommendations" />
  </div>
</template>