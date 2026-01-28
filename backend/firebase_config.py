import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the path from environment variable, default to current directory
config_path = os.getenv('FIREBASE_CONFIG_PATH', 'serviceAccountKey.json')

# Initialize Firebase
cred = credentials.Certificate(config_path)
firebase_admin.initialize_app(cred)

db = firestore.client()