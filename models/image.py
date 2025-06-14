class Image:
    def __init__(self, name: str, path: str, collection: str):
        self.name = name
        self.path = path
        self.collection = collection

    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path,
            "collection": self.collection
        }
