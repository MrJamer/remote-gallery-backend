class CollectionService:
    def __init__(self):
        self.collections = {}

    def create_collection(self, name):
        if name not in self.collections:
            self.collections[name] = []
        return {"status": "created", "name": name}

    def add_image_to_collection(self, collection_name, image_id):
        if collection_name in self.collections:
            self.collections[collection_name].append(image_id)
            return {"status": "added"}
        return {"status": "collection not found"}
