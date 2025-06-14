from models.image import Image
from utils.file_manager import save_image_file

class GalleryService:
    def __init__(self):
        self.images = []

    def upload_image(self, name, path, collection):
        image = Image(name, path, collection)
        save_image_file(path)  # Тут буде логіка збереження
        self.images.append(image)
        return image

    def list_images(self):
        return [img.to_dict() for img in self.images]
