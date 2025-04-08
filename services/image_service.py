from models.image import Image
from utils.db import db
from utils.exceptions import ModelNotFoundException

def save_image(img: Image) -> Image:
    db.session.add(img)
    db.session.commit()

    return img

def get_image_by_id(id: int) -> Image:
    image = Image.query.get(id)
    if not image:
        raise ModelNotFoundException("Image", "image")
    return image