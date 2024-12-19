import { GoogleGenerativeAI } from '@google/generative-ai'
import type { MusicPreferences, RecommendationResult } from '../types/music'

const API_KEY = import.meta.env.VITE_GEMINI_API_KEY

export class AIService {
  private static instance: AIService
  private genAI: GoogleGenerativeAI

  private constructor() {
    if (!API_KEY) {
      throw new Error('Gemini API key is not configured')
    }
    this.genAI = new GoogleGenerativeAI(API_KEY)
  }

  public static getInstance(): AIService {
    if (!AIService.instance) {
      AIService.instance = new AIService()
    }
    return AIService.instance
  }

  public async getRecommendations(preferences: MusicPreferences): Promise<RecommendationResult> {
    try {
      const model = this.genAI.getGenerativeModel({ model: 'gemini-pro' })
      
      const prompt = this.buildPrompt(preferences)
      const result = await model.generateContent(prompt)
      const response = await result.response
      const text = response.text()
      
      return {
        songs: text.split('\n').filter(line => line.trim())
      }
    } catch (error) {
      console.error('Error getting recommendations:', error)
      return {
        songs: [],
        error: 'Failed to get recommendations. Please try again later.'
      }
    }
  }

  private buildPrompt(preferences: MusicPreferences): string {
    return `Recommend 5 songs that are:
    - In ${preferences.language}
    - From the ${preferences.decade}
    - Genre: ${preferences.genre}
    - Mood: ${preferences.mood}
    ${preferences.favoriteArtist ? `- Similar to: ${preferences.favoriteArtist}` : ''}
    
    Format each song as: "Artist - Song Title"`
  }
}