from models.db_models import Image
from repositories.image_repository import ImageRepository

class ImageService:
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    def upload_image(self, filename: str, path: str, collection_id: int):
        image = Image(filename=filename, path=path, collection_id=collection_id)
        return self.repository.save_image(image)

    def fetch_image(self, image_id: int):
        return self.repository.get_image(image_id)
