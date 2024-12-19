import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # You need to download Tesseract and link to the .exe here.

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    image_cropped = image.crop((0, 0, image.width, 30))
    image_cropped = image_cropped.resize((image_cropped.width * 3, image_cropped.height * 3), Image.Resampling.LANCZOS)
    text = pytesseract.image_to_string(image_cropped)

    text = text.split(' BY')[0] # Remove the text after the word 'by' (including 'by' itself).

    # Clean the text to make it a valid filename (remove invalid characters)
    valid_filename = ''.join(e for e in text if e.isalnum() or e in (' ', '_')).strip()

    return valid_filename

def rename_image(image_path):
    new_name = extract_text_from_image(image_path)
    file_extension = os.path.splitext(image_path)[1]
    new_image_path = os.path.join(os.path.dirname(image_path), f"{new_name}{file_extension}")

    # Check if the file already exists, and if so, append a number to make it unique.
    counter = 1
    while os.path.exists(new_image_path):
        new_image_path = os.path.join(os.path.dirname(image_path), f"{new_name}_{counter}{file_extension}")
        counter += 1

    os.rename(image_path, new_image_path)

    print(f"Image {image_path} renamed to: {new_image_path}")

# Iterate over all .png files in the ./comics/ directory.
comics_folder = './comics/'
for filename in os.listdir(comics_folder):
    if filename.endswith('.png'):
        image_path = os.path.join(comics_folder, filename)
        rename_image(image_path)
