from .user_seeder import seed_users
from .company_seeder import seed_companies
from .specialization_seeder import seed_specializations
from .post_seeder import seed_posts
from .like_seeder import seed_likes

def seed_all():
    """Ejecuta todos los seeders si no hay datos en la base de datos."""
    from services.user_service import get_all_users
    from services.company_service import get_all_companies
    from services.post_service import get_all_posts
    from services.specialization_service import get_all_specializations
    from services.like_service import get_all_like

    if not get_all_users():
        seed_users()
    if not get_all_companies():
        seed_companies()
    if not get_all_specializations():
        seed_specializations()
    if not get_all_posts():
        seed_posts()
    if not get_all_like():
        seed_likes(200)
