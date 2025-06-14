from services.gallery_service import GalleryService

class GalleryController:
    def __init__(self):
        self.service = GalleryService()

    def upload(self, name, path, collection):
        return self.service.upload_image(name, path, collection)

    def get_all(self):
        return self.service.list_images()
