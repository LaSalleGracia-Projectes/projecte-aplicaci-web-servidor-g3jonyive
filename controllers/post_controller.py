from utils.utils import make_error_response, is_admin_token
import services.post_service as service
from utils.exceptions import InternalServerError, ValidationError, ModelNotFoundException, UnauthorizedException, FirebaseException
import validators.post_validator as validator
from utils.firebase_utils import get_user_by_token
from models.post import Post

def get_all_posts():
    try:
        return [post.serialize() for post in service.get_all_posts()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))

def add_post(data: dict):
    try:
        user = get_user_by_token()
        
        data['user_id'] = user.id
        
        validator.validate_add_post(data)
        
        post = service.add_post(Post(**data))
        
        return post.serialize(), 201
    except (ValidationError, FirebaseException, ModelNotFoundException, UnauthorizedException) as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))
    
def get_post_by_id(post_id: int):
    try:
        return service.get_post_by_id(post_id).serialize(), 200
    except ModelNotFoundException as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))
    
def delete_post(post_id: int):
    try:
        if is_admin_token():
            return service.delete_post(post_id), 204
        
        user = get_user_by_token()
        
        post = service.get_post_by_id(post_id)
        
        if post.user_id != user.id:
            raise UnauthorizedException("You are not authorized to delete this post")
        
        return service.delete_post(post_id), 204
    except (ModelNotFoundException, UnauthorizedException) as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))