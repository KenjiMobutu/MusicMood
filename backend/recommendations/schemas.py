from pydantic import BaseModel
from typing import List
from datetime import datetime

class MusicPreferences(BaseModel):
    language: str
    decade: str
    genre: str
    mood: str
    favorite_artist: str = None

class RecommendationCreate(BaseModel):
    preferences: MusicPreferences

class RecommendationResponse(BaseModel):
    id: int
    songs: List[str]
    preferences: MusicPreferences
    created_at: datetime