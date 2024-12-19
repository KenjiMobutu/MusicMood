from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    favorite_genres: Optional[List[str]] = []
    favorite_artists: Optional[List[str]] = []

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    favorite_genres: List[str]
    favorite_artists: List[str]

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"