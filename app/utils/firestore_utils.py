from config import PATH
import firebase_admin
from firebase_admin import credentials, firestore
from utils.utils import log

cred = credentials.Certificate(f"{PATH}/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
userCollection = db.collection("users")

def add_firestore_user(user_data: dict):
    """Agrega un usuario a Firestore."""
    
    log(f"Agregando usuario {user_data['uid']} a Firestore...")
    
    try:
        userCollection.document(user_data["uid"]).set(user_data)
        log("Usuario agregado a Firestore.")
    except Exception as e:
        log(f"Error al agregar el usuario a Firestore: {e}")
        
    log(f"Usuario {user_data['uid']} agregado a Firestore.")