import pytesseract
import cv2
import os
from rules import detect_red_flags

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = os.path.join(os.path.dirname(__file__), "scam1.jpeg")
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(
        f"Could not read image: {image_path}"
    )

#cv2.imshow("window", img)
#cv2.waitKey(0)  
#cv2.destroyAllWindows()

def clean_ocr_text(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    return "\n".join(lines)

raw_text = pytesseract.image_to_string(img)

cleaned_text = clean_ocr_text(raw_text)

red_flags = detect_red_flags(cleaned_text)

print("\n   RISK INDICATORS  \n")

if red_flags:
    for flag in red_flags:
        print(f" WARNING: {flag['category']} : {flag['matched_scam_message']} claim detected... \n")

else:
    print("No configured warning patterns detected.")