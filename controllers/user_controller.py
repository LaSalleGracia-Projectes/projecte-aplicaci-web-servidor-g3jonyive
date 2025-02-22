import services.user_service as service
from models import User
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException

def get_all_users():
    try:
        return [user.serialize() for user in service.get_all_users()], 200
    except Exception as e:
        return {"error": "Has occurred an error", "details": str(e)}, 500
    
def get_user_by_username(username: str):
    try:
        user = service.get_user_by_username(username)
        if not user:
            raise ModelNotFoundException("User", username)
        return user.serialize(), 200
    except ModelNotFoundException as e:
        return {"error": "Has occurred an error", "details": str(e)}, 404
    
def search_user_by_username(username: str):
    try:
        return [user.serialize() for user in service.search_user_by_username(username)], 200
    except Exception as e:
        return {"error": "Has occurred an error", "details": str(e)}, 500