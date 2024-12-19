import type { User } from './user'

export interface LoginCredentials {
  email: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
  favorite_genres: string[]
  favorite_artists: string[]
}

export interface AuthState {
  user: User | null
  token: string | null
  isAuthenticated: boolean
}