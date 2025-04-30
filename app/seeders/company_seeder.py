from faker import Faker
from models.company import Company
from services.company_service import add_company

fake = Faker()

def seed_companies(companies=10):
    """Genera compañías ficticias y las inserta en la base de datos."""
    for _ in range(companies):
        company = Company(
            name=fake.company(),
            logo=fake.image_url(),
            description=fake.text(),
        )
        add_company(company)

    print(f"Se han insertado {companies} compañías ficticias en la base de datos.")