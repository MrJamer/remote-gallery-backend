from sqlalchemy.orm import Session
from models.db_models import Image

class ImageRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_image(self, image: Image):
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)
        return image

    def get_image(self, image_id: int):
        return self.db.query(Image).filter(Image.id == image_id).first()
