import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import json
# try to push in github
# 1️⃣ Set the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 2️⃣ PDF file path (replace with your actual PDF path)
pdf_path = r"C:\Users\Dell\Downloads\Internship Agreement - Trufe Tech Private Limited - Mr Tanuj Dwivedi (1) (1).pdf"

# 3️⃣ Open the PDF
doc = fitz.open(pdf_path)

# 4️⃣ Prepare a list to store JSON data
data = []

# 5️⃣ Loop through each page
for i in range(len(doc)):
    page = doc[i]
    
    # Convert page to image
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # OCR: extract text
    text = pytesseract.image_to_string(img)
    
    # Add to JSON structure
    data.append({
        "page_number": i + 1,
        "text": text.strip()
    })

# 6️⃣ Convert to JSON string
json_output = json.dumps(data, ensure_ascii=False, indent=4)

# 7️⃣ Print JSON (optional)
print(json_output) 
print("tanuj dwivedi")

# 8️⃣ Save JSON to a file
# with open("output.json", "w", encoding="utf-8") as f:
#     f.write(json_output)

# print("\n✅ OCR complete! JSON saved as 'output.json'.")

# pdf.output("ocr_output.pdf") # pyright: ignore[reportUndefinedVariable]

# print("✅ JSON saved as PDF: 'ocr_output.pdf'")