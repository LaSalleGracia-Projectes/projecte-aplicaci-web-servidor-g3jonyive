from flask import request
from utils.utils import make_error_response, is_admin_token
import services.specialization_service as service
from models import Specialization
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException, ValidationError, InternalServerError, UnauthorizedException

def get_all_specializations():
    try:
        return [specialization.serialize() for specialization in service.get_all_specializations()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))