from ninja import Router
from typing import List
from .schemas import RecommendationCreate, RecommendationResponse
from .models import Recommendation
from .services import get_ai_recommendations

router = Router()

@router.post("/", response=RecommendationResponse)
def create_recommendation(request, data: RecommendationCreate):
    songs = get_ai_recommendations(data.preferences)
    recommendation = Recommendation.objects.create(
        user=request.user,
        songs=songs,
        preferences=data.preferences.dict()
    )
    return recommendation

@router.get("/history", response=List[RecommendationResponse])
def get_recommendation_history(request):
    recommendations = Recommendation.objects.filter(user=request.user)
    return recommendations