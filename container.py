from services.user_service import UserService
from services.image_service import ImageService
from services.collection_service import CollectionService

class Container:
    def __init__(self):
        self._services = {}
        self.register_services()

    def register(self, key, service):
        self._services[key] = service

    def resolve(self, key):
        return self._services.get(key)

    def register_services(self):
        self.register("user_service", UserService())
        self.register("image_service", ImageService())
        self.register("collection_service", CollectionService())

container = Container()
