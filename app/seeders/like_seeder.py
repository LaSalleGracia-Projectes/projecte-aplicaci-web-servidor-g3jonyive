from faker import Faker
from models.like import Like
from services.like_service import add_like
from utils.utils import log

fake = Faker()

def seed_likes(likes=10):
    """Genera likes ficticios y los inserta en la base de datos."""
    log(f"Iniciando la inserción de {likes} likes ficticios...")
    
    for _ in range(likes):
        like = Like(
            user_id=fake.random_int(min=1, max=10),
            post_id=fake.random_int(min=1, max=10),
        )
        add_like(like)

    log(f"Se han insertado {likes} likes ficticios en la base de datos.")