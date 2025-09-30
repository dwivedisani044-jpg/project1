import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import json

# Step 1: Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 2: Load the image
image_path = r"C:\Users\Dell\Downloads\WhatsApp Image 2025-08-21 at 1.18.17 PM.jpeg"
image = Image.open(image_path)

# ✅ Step 3: Preprocess image for better accuracy

# Convert to grayscale
image = image.convert("L")

# Increase contrast
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2)

# Sharpen
image = image.filter(ImageFilter.SHARPEN)

# Resize (helps if the text is small)
image = image.resize((image.width * 2, image.height * 2))

# ✅ Step 4: OCR with better config
config = r'--oem 3 --psm 6'   # You can change psm 6 to psm 4 or psm 11 if needed
extracted_text = pytesseract.image_to_string(image, config=config)

# ✅ Step 5: Print output
print("Extracted Text:\n")
print(extracted_text)

# ✅ Step 6: Save to JSON
data = {
    "file_name": "myimage.jpeg",
    "extracted_text": extracted_text
}

with open("extracted_text.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Text saved to extracted_text.json successfully!")
