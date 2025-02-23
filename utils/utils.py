from utils.constants import ERROR_RESPONSE
from config import DEBUG
from flask import request
from utils.exceptions import BadRequestException
from werkzeug.exceptions import BadRequest

def log(tag: str = "[DEBUG]", message: str = "") -> None:
    if DEBUG:
        print(f"{tag} {message}")
        
def make_error_response(exception: Exception) -> dict:
    return {"error": ERROR_RESPONSE, "details": exception.details, "exception": type(exception).__name__}, exception.status_code

def need_json(func):
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return make_error_response(BadRequestException())
        
        try:
            data = request.get_json()
        except BadRequest as e:
            e = BadRequestException(str(e))
            return make_error_response(e)
        
        return func(*args, **kwargs)
    return wrapper