from utils.database import init_db, SessionLocal
from repositories.image_repository import ImageRepository
from services.image_service import ImageService

def main():
    init_db()
    
    db = SessionLocal()
    image_repo = ImageRepository(db)
    image_service = ImageService(image_repo)

    new_image = image_service.upload_image("pic1.png", "/images/pic1.png", 1)
    print("Saved:", new_image.filename)

    retrieved = image_service.fetch_image(new_image.id)
    print("Retrieved:", retrieved.filename)

if __name__ == "__main__":
    main()
