from faker import Faker
from models.company import Company
from services.company_service import add_company
from utils.utils import log

fake = Faker()

def seed_companies(companies=10):
    """Genera compañías ficticias y las inserta en la base de datos."""
    log(f"Iniciando la inserción de {companies} compañías ficticias...")
    
    for _ in range(companies):
        company = Company(
            name=fake.company(),
            logo="https://picsum.photos/200",
            description=fake.text(),
        )
        add_company(company)

    log(f"Se han insertado {companies} compañías ficticias en la base de datos.")