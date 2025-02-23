from utils.db import db
from models.post import Post

def get_all_posts() -> list:
    return Post.query.all()