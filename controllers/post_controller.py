from utils.utils import make_error_response
import services.post_service as service
from utils.exceptions import InternalServerError, ValidationError
import validators.post_validator as validator
from utils.firebase_utils import get_user_by_token
from models.post import Post

def get_all_posts():
    try:
        return [post.serialize() for post in service.get_all_posts()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))

@get_user_by_token
def add_post(data: dict):
    try:
        validator.validate_add_post(data)
        
        post = service.add_post(Post(**data))
        
        return post.serialize(), 201
    except ValidationError as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))