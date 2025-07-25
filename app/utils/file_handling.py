import os 
import shutil
from fastapi import UploadFile

def save_uploaded_file(file: UploadFile, upload_dir="uploads"):
    os.makedirs(upload_dir, exist_ok=True)
    file_location = os.path.join(upload_dir, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_location
