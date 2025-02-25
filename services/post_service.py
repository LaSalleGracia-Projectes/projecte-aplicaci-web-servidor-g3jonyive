from utils.db import db
from models.post import Post
from utils.exceptions import ModelNotFoundException

def get_all_posts() -> list:
    return Post.query.all()

def add_post(post: Post) -> Post:
    db.session.add(post)
    db.session.commit()
    return post

def get_post_by_id(post_id: int) -> Post:
    post = Post.query.get(post_id)
    if not post:
        raise ModelNotFoundException("Post", post_id)
    return post