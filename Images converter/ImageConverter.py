import sys
import os
from PIL import Image

def get_image_list(folder_path):
    image = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img = Image.open(file_path)
            image.append(img)
    return image

def check_exist_path(folder_path):
    return os.path.exists(folder_path)

def save_to_png(images:list , png_folder_path,jpeg_path,format:str):
    os.makedirs(png_folder_path, exist_ok=True)
    for img in images:
        file_name = os.path.splitext(os.path.basename(jpeg_path + os.path.splitext(img.filename)[0]))[1]
        png_path = os.path.join(png_folder_path, f"{file_name}.{format.lower()}")
        print(file_name)
        img.save(png_path, format.upper())

format = sys.argv[1] 
get_folder = "pics"
set_folder = "convert pics"
images = []

if not check_exist_path(get_folder): 
    sys.exit("The folder does not exist")
images = get_image_list(get_folder)
save_to_png(images,set_folder,get_folder,format)
print("is done correctly")



    