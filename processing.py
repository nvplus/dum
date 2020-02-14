from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_image_text(filename):
    img = Image.open(filename)
    out = pytesseract.image_to_string(img)

    return out