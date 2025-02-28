from flask import request
from utils.utils import make_error_response, is_admin_token
import services.company_service as service
from models import Company
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException, ValidationError, InternalServerError, UnauthorizedException

def get_all_companies():
    try:
        return [company.serialize() for company in service.get_all_companies()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))
