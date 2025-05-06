from config import PATH
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(f"{PATH}/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
userCollection = db.collection("users")

def add_firestore_user(user_data):
    """Agrega un usuario a Firestore."""
    try:
        userCollection.add(user_data)
        print("Usuario agregado a Firestore.")
    except Exception as e:
        print(f"Error al agregar el usuario a Firestore: {e}")