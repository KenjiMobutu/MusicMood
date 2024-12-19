from ninja import Router
from django.contrib.auth import authenticate
from .schemas import UserCreate, UserLogin, UserResponse, Token
from .models import User
from .auth import create_access_token, get_password_hash

router = Router()

@router.post("/register", response=UserResponse)
def register(request, user_data: UserCreate):
    user = User.objects.create(
        username=user_data.username,
        email=user_data.email,
        password=get_password_hash(user_data.password),
        favorite_genres=user_data.favorite_genres,
        favorite_artists=user_data.favorite_artists
    )
    return user

@router.post("/login", response=Token)
def login(request, user_data: UserLogin):
    user = authenticate(email=user_data.email, password=user_data.password)
    if not user:
        return {"error": "Invalid credentials"}
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token}

@router.get("/me", response=UserResponse)
def get_current_user(request):
    user = request.user
    return user