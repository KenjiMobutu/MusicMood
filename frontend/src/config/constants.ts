export const LANGUAGES = ['English', 'French', 'Spanish', 'German'] as const
export const DECADES = ['60s', '70s', '80s', '90s', '2000s', '2010s', '2020s'] as const
export const GENRES = ['Pop', 'Rock', 'Hip Hop', 'Jazz', 'Classical', 'Electronic', 'R&B'] as const
export const MOODS = ['Happy', 'Sad', 'Energetic', 'Relaxed', 'Romantic'] as const

export type Language = typeof LANGUAGES[number]
export type Decade = typeof DECADES[number]
export type Genre = typeof GENRES[number]
export type Mood = typeof MOODS[number]