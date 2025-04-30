from faker import Faker
from models.user import User
from services.user_service import add_user

fake = Faker()

def seed_users(users=10):
    """Genera usuarios ficticios y los inserta en la base de datos."""
    for _ in range(users):
        user = User(
            uid=fake.uuid4(),
            email=fake.email(),
            full_name=fake.name(),
            username=fake.user_name(),
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
            profile_picture=fake.image_url(),
            phone=fake.phone_number()
        )
        add_user(user)
    
    print(f"Se han insertado {users} usuarios ficticios en la base de datos.")