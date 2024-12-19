import type { Language, Decade, Genre, Mood } from '../config/constants'

export interface MusicPreferences {
  language: Language
  decade: Decade
  genre: Genre
  mood: Mood
  favoriteArtist?: string
}

export interface RecommendationResult {
  songs: string[]
  error?: string
}