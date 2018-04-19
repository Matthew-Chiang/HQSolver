import numpy
import cv2
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

import savePic

def getStr(filename):
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # It's important to include double quotes around the dir path.
    Im= Image.open(filename)
    arr=numpy.array(Im).reshape(Im.size[1],Im.size[0],3)

    #pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

    arr = cv2.resize(arr, (0,0), fx=3, fy=3)

    ret, image = cv2.threshold(arr,200,255,cv2.THRESH_BINARY)

    #kernel = numpy.ones((5,5),numpy.float32)/25
    #image = cv2.filter2D(image,-1,kernel)

    image = Image.fromarray(image,'RGB')

    savePic.savePic(image)

    #image.show()

    txt = pytesseract.image_to_string(image,config=tessdata_dir_config,lang="eng")#,lang="Circular")

    txt = txt.replace ("ﬁ","fi")

    return txt


#print(getStr("Screenshots/exampleProduction.png"))
