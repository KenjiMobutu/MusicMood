from pymongo import MongoClient
from django.conf import settings
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Connexion à MongoDB
try:
    client = MongoClient(os.getenv("MONGODB_URI"))

    # Vérification de la connexion
    client.server_info()  # Cela lève une exception si la connexion échoue

    # Récupérer la base de données
    db = client[os.getenv("MONGODB_NAME")]

    # Collections accessibles
    users_collection = db['users']
    songs_collection = db['songs']
    recommendations_collection = db['recommendations']

    print("Connexion à MongoDB réussie!")
except Exception as e:
    print(f"Erreur de connexion à MongoDB: {e}")
