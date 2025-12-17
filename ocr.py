from pdf2image import convert_from_path
import pytesseract

# Convert PDF file into images
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pages = convert_from_path("book.pdf")

# Run OCR scan on images
full_text = ""
for page in pages:
    text = pytesseract.image_to_string(page)
    full_text += text + "\n"

# Write text in a file
with open("new_ocr.txt", "w") as file:
    file.write(full_text)