from faker import Faker
from models.user import User
from services.user_service import add_user
import random

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
            profile_picture=get_random_image(),
            phone=fake.phone_number()
        )
        add_user(user)
    
    print(f"Se han insertado {users} usuarios ficticios en la base de datos.")
    
def get_random_image(style="personas", size=200, format="png"):
    """Genera una URL de avatar aleatoria usando DiceBear."""
    random_seed = ''.join(str(random.randint(0, 9)) for _ in range(10))
    return (
        f"https://api.dicebear.com/7.x/{style}/{format}"
        f"?size={size}&seed={random_seed}&flip=true"
    )