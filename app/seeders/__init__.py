from .user_seeder import seed_users
from services.user_service import get_all_users

def seed_all():
    """Función principal para ejecutar todos los seeders."""
    if len(get_all_users()) == 0:
        seed_users(10)
    