import { ref } from 'vue'
import type { LoginCredentials, RegisterData, AuthState } from '../types/auth'
import type { User } from '../types/user'

const API_URL = 'http://localhost:8000/api'

export class AuthService {
  private static instance: AuthService
  private state: AuthState = {
    user: null,
    token: localStorage.getItem('token'),
    isAuthenticated: false
  }

  private constructor() {
    if (this.state.token) {
      this.fetchUser()
    }
  }

  public static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService()
    }
    return AuthService.instance
  }

  public async login(credentials: LoginCredentials): Promise<void> {
    try {
      const response = await fetch(`${API_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      })

      if (!response.ok) throw new Error('Invalid credentials')

      const data = await response.json()
      this.setToken(data.access_token)
      await this.fetchUser()
    } catch (error) {
      throw new Error('Login failed')
    }
  }

  public async register(data: RegisterData): Promise<void> {
    try {
      const response = await fetch(`${API_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      })

      if (!response.ok) throw new Error('Registration failed')

      const userData = await response.json()
      await this.login({
        email: data.email,
        password: data.password
      })
    } catch (error) {
      throw new Error('Registration failed')
    }
  }

  public logout(): void {
    localStorage.removeItem('token')
    this.state.user = null
    this.state.token = null
    this.state.isAuthenticated = false
  }

  private async fetchUser(): Promise<void> {
    try {
      const response = await fetch(`${API_URL}/auth/me`, {
        headers: {
          'Authorization': `Bearer ${this.state.token}`
        }
      })

      if (!response.ok) throw new Error('Failed to fetch user')

      const user = await response.json()
      this.state.user = user
      this.state.isAuthenticated = true
    } catch (error) {
      this.logout()
    }
  }

  private setToken(token: string): void {
    localStorage.setItem('token', token)
    this.state.token = token
  }

  public getState(): AuthState {
    return this.state
  }
}