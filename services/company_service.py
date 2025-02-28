from utils.db import db
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException
from models.company import Company
from datetime import datetime

def get_all_companies() -> list:
    return Company.query.all()