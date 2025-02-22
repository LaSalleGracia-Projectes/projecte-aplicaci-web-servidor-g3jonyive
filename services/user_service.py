from utils.db import db
from utils.exceptions import ModelNotFoundException, ModelAlreadyExistsException
from models.user import User
from datetime import datetime

def add_user(user: User) -> User:
    try:
        get_user_by_uid(user.uid)
        get_user_by_email(user.email)
        get_user_by_username(user.username)
        raise ModelAlreadyExistsException("User", user.uid)
    except ModelNotFoundException as e:
        pass
    
    if isinstance(user.birth_date, str):
        user.birth_date = datetime.strptime(user.birth_date, "%Y-%m-%d").date()
    
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_uid(uid: str) -> User:
    user = User.query.filter_by(uid=uid).first()
    if not user:
        raise ModelNotFoundException("User", uid)
    return user

def get_user_by_email(email: str) -> User:
    user = User.query.filter_by(email=email).first()
    if not user:
        raise ModelNotFoundException("User", email)
    return user

def get_user_by_username(username: str) -> User:
    user = User.query.filter_by(username=username).first()
    if not user:
        raise ModelNotFoundException("User", username)
    return user

def get_user_by_id(id: str) -> User:
    user = User.query.get(id)
    if not user:
        raise ModelNotFoundException("User", id)
    return user

def get_all_users() -> list:
    return User.query.all()

def search_user_by_username(username: str) -> list:
    return User.query.filter(User.username.like(f"%{username}%")).all()

def delete_user_by_uid(uid: str):
    user = User.query.get(uid=uid)
    
    if not user:
        raise ModelNotFoundException("User", uid)
    
    db.session.delete(user)
    db.session.commit()

def update_user_by_id(user: User) -> User:
    old_user = User.query.get(user.id)
    
    if not old_user:
        raise ModelNotFoundException("User", user.username)
    
    old_user.uid = user.uid
    old_user.email = user.email
    old_user.username = user.username
    old_user.birth_date = user.birth_date
    old_user.phone = user.phone
    
    db.session.commit()
    return old_user
    