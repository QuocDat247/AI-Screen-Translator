import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab
from deep_translator import GoogleTranslator
import time
import hashlib
import threading
import tkinter as tk
import re

OCR_CONFIG = r'--oem 3 --psm 6' 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

last_hash = None

root = tk.Tk()
root.title("AI Translate - Auto Detect")
root.geometry("500x350")
root.attributes("-topmost", True)

text_box = tk.Text(root, wrap="word", font=("Arial", 11))
text_box.pack(expand=True, fill="both", padx=5, pady=5)

def update_ui(content):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, content)

def clean_text(text):
    if not text: return ""
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,!?])", r"\1", text)
    return text.strip()

def get_image_hash(img_np):
    return hashlib.md5(img_np.tobytes()).hexdigest()

def process_image(img):
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    raw_text = pytesseract.image_to_string(gray, lang='eng+jpn+chi_sim+chi_tra+kor+fra+deu+vie+ara+rus') 
    text = clean_text(raw_text)

    if not text or len(text) < 2:
        print("⚠️ Không nhận diện được chữ rõ ràng")
        return

    print("\n=== VĂN BẢN GỐC ===")
    print(text)

    try:
        translator = GoogleTranslator(source='auto', target='vi')
        
        translated = translator.translate(text)
        
        translated = clean_text(translated)

        print("=== BẢN DỊCH (AUTO) ===")
        print(translated)

        full_text = f"GỐC:\n{text}\n\n------------------\nDỊCH:\n{translated}"
        root.after(0, update_ui, full_text)

    except Exception as e:
        print("❌ Lỗi dịch:", e)
        root.after(0, update_ui, f"Lỗi dịch: {e}")

def watch_clipboard():
    global last_hash
    print("🟢 Đang theo dõi Clipboard (Win + Shift + S)...")
    
    while True:
        try:
            img = ImageGrab.grabclipboard()
            if img is not None:
                img_np = np.array(img)
                current_hash = get_image_hash(img_np)

                if current_hash != last_hash:
                    last_hash = current_hash
                    process_image(img)
        except Exception as e:
            print(f"Lỗi đọc Clipboard: {e}")
            
        time.sleep(1)

threading.Thread(target=watch_clipboard, daemon=True).start()
root.mainloop()