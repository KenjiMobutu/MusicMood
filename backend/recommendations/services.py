from google.generativeai import GenerativeModel
import os
from typing import List
from .schemas import MusicPreferences

def get_ai_recommendations(preferences: MusicPreferences) -> List[str]:
    model = GenerativeModel('gemini-pro')
    
    prompt = f"""Recommend 5 songs that are:
    - In {preferences.language}
    - From the {preferences.decade}
    - Genre: {preferences.genre}
    - Mood: {preferences.mood}
    {f'- Similar to: {preferences.favorite_artist}' if preferences.favorite_artist else ''}
    
    Format each song as: "Artist - Song Title"
    """
    
    response = model.generate_content(prompt)
    songs = response.text.split('\n')
    return [song.strip() for song in songs if song.strip()]