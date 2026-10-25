import os
from pymongo import MongoClient

# Replace <username> and <password> with your MongoDB credentials
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["Drowsi"]  # Database Name
users_collection = db["Drowsi"]  # Collection Name
