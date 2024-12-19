<script setup lang="ts">
defineProps<{
  songs: string[]
}>()
</script>

<template>
  <div v-if="songs.length > 0" class="bg-white rounded-lg shadow-md p-6">
    <h3 class="text-xl font-semibold mb-4">Your Recommended Songs</h3>
    <ul class="space-y-2">
      <li
        v-for="(song, index) in songs"
        :key="index"
        class="p-3 bg-gray-50 rounded-md hover:bg-gray-100 transition-colors"
      >
        {{ song }}
      </li>
    </ul>
  </div>
</template>