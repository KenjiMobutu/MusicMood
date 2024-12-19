# users/views.py
from django.http import JsonResponse
from pymongo import MongoClient
from django.conf import settings

# Connexion à MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        favorite_genres = data.get('favorite_genres', [])
        favorite_artists = data.get('favorite_artists', [])

        # Vérifiez si l'utilisateur existe déjà
        existing_user = db.users.find_one({'email': email})
        if existing_user:
            return JsonResponse({'error': 'Email already in use'}, status=400)

        # Créez un nouvel utilisateur
        user = {
            'username': username,
            'email': email,
            'favorite_genres': favorite_genres,
            'favorite_artists': favorite_artists
        }
        db.users.insert_one(user)

        return JsonResponse({'message': 'User created successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
