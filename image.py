import pytesseract
from PIL import Image
import json

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r"C:\Users\Dell\Downloads\WhatsApp Image 2025-08-21 at 1.18.17 PM.jpeg" #  image path

image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)

print("Extracted Text:\n")
print(extracted_text)

data = {
    "file_name": "myimage.png",
    "extracted_text": extracted_text
}

with open("extracted_text.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Text saved to extracted_text.json successfully!")