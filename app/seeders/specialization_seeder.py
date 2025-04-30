from faker import Faker
from models.specialization import Specialization
from services.specialization_service import add_specialization

fake = Faker()

def seed_specializations(specializations=10):
    """Genera especializaciones ficticias y las inserta en la base de datos."""
    for _ in range(specializations):
        specialization = Specialization(
            name=fake.company(),
            description=fake.text(),
        )
        add_specialization(specialization)

    print(f"Se han insertado {specializations} especializaciones ficticias en la base de datos.")