from pymongo import MongoClient
from django.conf import settings
import os
from dotenv import load_dotenv

# Connexion à MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("MONGODB_NAME")]

# Collections accessibles
users_collection = db['users']
songs_collection = db['songs']
recommendations_collection = db['recommendations']
