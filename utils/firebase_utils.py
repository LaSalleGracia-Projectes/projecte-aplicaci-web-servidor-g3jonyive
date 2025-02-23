import pyrebase
from config import FIREBASECONFIG, ADMIN_TOKEN
from requests.exceptions import HTTPError
from utils.exceptions import FirebaseException, UnauthorizedException, ModelNotFoundException
from flask import request
from services.user_service import get_user_by_username
from utils.utils import make_error_response

firebase = pyrebase.initialize_app(FIREBASECONFIG)
auth = firebase.auth()

def verify_token(token: str) -> str:
    try:
        user = auth.get_account_info(token)
        return user['users'][0]['localId']
    except HTTPError as e:
        raise FirebaseException(e)
    
def verify_token_username(func):
    def wrapper(username, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return make_error_response(UnauthorizedException())
        
        if auth_header == ADMIN_TOKEN:
            return func(username, *args, **kwargs)
        
        try:
            uid_user = verify_token(auth_header)
        except FirebaseException as e:
            return make_error_response(e)
        try:
            user = get_user_by_username(username)
        except ModelNotFoundException as e:
            return make_error_response(e)
        
        if user.uid != uid_user:
            return make_error_response(UnauthorizedException())
        
        return func(username, *args, **kwargs)
    return wrapper

def verify_token_uid(func):
    def wrapper(uid, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return make_error_response(UnauthorizedException())
        
        if auth_header == ADMIN_TOKEN:
            return func(uid, *args, **kwargs)
        
        try:
            uid_user = verify_token(auth_header)
        except FirebaseException as e:
            return make_error_response(e)
        
        if uid != uid_user:
            return make_error_response(UnauthorizedException())
        
        return func(uid, *args, **kwargs)
    return wrapper
