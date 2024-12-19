<script setup lang="ts">
import { ref } from 'vue'
import type { MusicPreferences } from '../types/music'
import { LANGUAGES, DECADES, GENRES, MOODS } from '../config/constants'

const emit = defineEmits<{
  (e: 'submit', preferences: MusicPreferences): void
}>()

const language = ref(LANGUAGES[0])
const decade = ref(DECADES[3]) // '90s'
const genre = ref(GENRES[0])
const mood = ref(MOODS[0])
const favoriteArtist = ref('')

function handleSubmit() {
  emit('submit', {
    language: language.value,
    decade: decade.value,
    genre: genre.value,
    mood: mood.value,
    favoriteArtist: favoriteArtist.value || undefined
  })
}
</script>

<template>
  <div class="bg-white rounded-lg shadow-md p-6 mb-6">
    <h2 class="text-2xl font-semibold mb-6">Find Your Perfect Music Match</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
      <div class="space-y-2">
        <label class="block text-sm font-medium text-gray-700">Language</label>
        <select v-model="language" class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
          <option v-for="lang in LANGUAGES" :key="lang" :value="lang">{{ lang }}</option>
        </select>
      </div>

      <div class="space-y-2">
        <label class="block text-sm font-medium text-gray-700">Decade</label>
        <select v-model="decade" class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
          <option v-for="dec in DECADES" :key="dec" :value="dec">{{ dec }}</option>
        </select>
      </div>

      <div class="space-y-2">
        <label class="block text-sm font-medium text-gray-700">Genre</label>
        <select v-model="genre" class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
          <option v-for="g in GENRES" :key="g" :value="g">{{ g }}</option>
        </select>
      </div>

      <div class="space-y-2">
        <label class="block text-sm font-medium text-gray-700">Mood</label>
        <select v-model="mood" class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
          <option v-for="m in MOODS" :key="m" :value="m">{{ m }}</option>
        </select>
      </div>

      <div class="space-y-2 md:col-span-2">
        <label class="block text-sm font-medium text-gray-700">Favorite Artist (Optional)</label>
        <input
          v-model="favoriteArtist"
          type="text"
          class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          placeholder="Enter an artist name"
        >
      </div>
    </div>

    <button
      @click="handleSubmit"
      class="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
    >
      Get Recommendations
    </button>
  </div>
</template>