from utils.db import db
from models.post import Post

def get_all_posts() -> list:
    return Post.query.all()

def add_post(post: Post) -> Post:
    db.session.add(post)
    db.session.commit()
    return post