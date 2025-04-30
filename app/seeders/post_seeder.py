from faker import Faker
from models.post import Post
from services.post_service import add_post

fake = Faker()

def seed_posts(posts=10):
    """Genera publicaciones ficticias y las inserta en la base de datos."""
    for _ in range(posts):
        post = Post(
            title=fake.sentence(),
            description=fake.text(),
            price=round(fake.random_number(digits=2, fix_len=True) + fake.random.random(), 2),
            user_id=fake.random_int(min=1, max=10),
            photo=fake.image_url(),
            company_id=fake.random_int(min=1, max=10),
            specialization_id=fake.random_int(min=1, max=10),
            created_at=fake.date_time_this_year()
        )
        add_post(post)

    print(f"Se han insertado {posts} publicaciones ficticias en la base de datos.")