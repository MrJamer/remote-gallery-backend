import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded_images")

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def save_image_file(file_path):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filename = os.path.basename(file_path)
    dest = os.path.join(UPLOAD_DIR, filename)
    shutil.copy(file_path, dest)
    return dest
