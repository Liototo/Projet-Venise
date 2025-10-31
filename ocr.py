from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

print('Converting pdf into images...')
pages = convert_from_path("book.pdf", poppler_path=r"C:\Users\lioto\Documents\poppler-25.07.0\Library\bin")

full_text = ""

print('Done!\n\nRunning OCR on pages...')
for page in pages:
    text = pytesseract.image_to_string(page)
    full_text += text + "\n"

print('Done!\n\nWriting into file...')
with open("new_ocr.txt", "w") as file:
    file.write(full_text)

print('Done! Your PDF is all transcribed in new_ocr.txt!')