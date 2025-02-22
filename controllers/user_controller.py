from utils.utils import make_error_response
import services.user_service as service
from models import User
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException, ValidationError
from validators import user_validator as validator

def get_all_users():
    try:
        return [user.serialize() for user in service.get_all_users()], 200
    except Exception as e:
        return make_error_response(str(e), 500)
    
def get_user_by_username(username: str):
    try:
        user = service.get_user_by_username(username)
        if not user:
            raise ModelNotFoundException("User", username)
        return user.serialize(), 200
    except ModelNotFoundException as e:
        return make_error_response(str(e), 404)
    
def search_user_by_username(username: str):
    try:
        return [user.serialize() for user in service.search_user_by_username(username)], 200
    except Exception as e:
        return make_error_response(str(e), 500)
    
def add_user(data: dict):
    try:
        validator.validate_add_user(data)
        user = User(**data)
        new_user = service.add_user(user)
        return new_user.serialize(), 201
    except ModelAlreadyExistsException as e:
        return make_error_response(str(e), 409)
    except ValidationError as e:
        return {"error": "Invalid fields", "details": e.errors}, 400
    except Exception as e:
        return make_error_response(str(e), 500)
    
def delete_user(username: str):
    try:
        return service.delete_user_by_username(username), 204
    except ModelNotFoundException as e:
        return make_error_response(str(e), 404)
    except Exception as e:
        return make_error_response(str(e), 500)