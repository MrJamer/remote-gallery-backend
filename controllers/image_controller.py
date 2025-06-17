from container import container

class ImageController:
    def __init__(self):
        self.image_service = container.resolve("image_service")

    def upload_image(self, image_data):
        return self.image_service.save_image(image_data)

    def get_image(self, image_id):
        return self.image_service.fetch_image(image_id)
