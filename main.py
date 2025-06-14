from logger_config import setup_logger
from controllers.gallery_controller import GalleryController

logger = setup_logger()

def main():
    controller = GalleryController()
    
    try:
        logger.info("Image loading.")
        image = controller.upload("cat.jpg", "examples/cat.jpg", "cats")
        logger.info(f"Image uploaded: {image.to_dict()}")

        images = controller.get_all()
        logger.info(f"All images: {images}")

    except Exception as e:
        logger.exception("Error executing main logic")

if __name__ == "__main__":
    main()
