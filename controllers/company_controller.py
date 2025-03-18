from flask import request
from utils.utils import make_error_response, is_admin_token
import services.company_service as service
from models import Company
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException, ValidationError, InternalServerError, UnauthorizedException
import validators.company_validator as validator

def get_all_companies():
    try:
        return [company.serialize() for company in service.get_all_companies()], 200
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))
    
def get_company_by_id(company_id: int):
    try:
        return service.get_company_by_id(company_id).serialize(), 200
    except ModelNotFoundException as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))

def delete_company(company_id: int):
    try:
        return service.delete_company(company_id), 204
    except (ModelNotFoundException, UnauthorizedException) as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))

def add_company(data):
    try:
        validated_data = validator.validate_add_company(data)
        company = service.add_company(Company(**validated_data))
        return company.serialize(), 201
    except (ValidationError, ModelAlreadyExistsException) as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))
    
def update_company(company_id: int, data):
    try:
        company = service.get_company_by_id(company_id)
        
        validated_data = validator.validate_update_company(data)
        
        company.name = validated_data.get("name", company.name)
        company.logo = validated_data.get("logo", company.logo)
        company.description = validated_data.get("description", company.description)
        
        company.id = company_id
        
        return service.update_company(company).serialize(), 200
    except (ValidationError, ModelNotFoundException) as e:
        return make_error_response(e)
    except Exception as e:
        return make_error_response(InternalServerError(str(e)))