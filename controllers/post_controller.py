from utils.utils import make_error_response
import services.post_service as service
from utils.exceptions import InternalServerError

def get_all_posts():
    try:
        return [post.serialize() for post in service.get_all_posts()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))