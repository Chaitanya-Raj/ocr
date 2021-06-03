from PIL import Image
from pathlib import Path
import sys
import os
import pytesseract
import numpy as np
import cv2

if len(sys.argv) < 2:
    print("> 'python3 ocr.py <path/to/file>'")
    sys.exit()

try:
    filename = Path(sys.argv[1])
    img = np.array(Image.open(filename))
except BaseException as e:
    print(e)
    sys.exit()
else:
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    text = pytesseract.image_to_string(img)
    print("\n")
    print(text)
    f_name, f_ext = os.path.splitext(os.path.basename(filename))
    if not os.path.exists('output'):
        os.makedirs('output')
    with open(f"output/{f_name}.txt", "w") as f:
        f.write(text)
