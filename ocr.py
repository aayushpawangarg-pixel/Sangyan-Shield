import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
import os

image_path = os.path.join(os.path.dirname(__file__), "scam1.jpeg")
img = cv2.imread(image_path)

cv2.imshow("window", img)
cv2.waitKey(0)  
cv2.destroyAllWindows()

#text = pytesseract.image_to_string(img)
#print("===== RAW OCR TEXT =====")
#print(text)

def clean_ocr_text(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)
    return "\n".join(lines)

raw_text = pytesseract.image_to_string(img)

cleaned_text = clean_ocr_text(raw_text)
'''print("===== CLEANED TEXT =====")
print(cleaned_text)'''

#detecting red flasgs in the text
def detect_red_flags(text):
    flags = []
    text_lower = text.lower()

    #  Guaranteed / unrealistic returns
    if any(word in text_lower for word in [ "guaranteed", "assured profit", "risk-free", "no loss", "fixed return"]):
        flags.append("Guaranteed or risk-free return claim")

    # Regulatory claims
    if any(phrase in text_lower for phrase in [ "sebi approved", "sebi registered", "government approved"]):
        flags.append("Regulatory approval claim")

    # Urgency
    if any(word in text_lower for word in [ "limited", "urgent", "act now", "today only", "last chance"]):
        flags.append("Urgency tactic")

    # Money request
    if any(word in text_lower for word in [ "invest", "send money", "transfer", "pay now", "deposit"]):
        flags.append("Request for money")
    return flags


red_flags = detect_red_flags(cleaned_text)
print("===== RED FLAGS =====")
for flag in red_flags:
    print("🚩", flag)