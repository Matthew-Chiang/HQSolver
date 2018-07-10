import pyautogui as pyau
from PIL import Image


pic = pyau.screenshot()

pic.save('Screenshots/realPic.png')

img = Image.open('Screenshots/realPic.png') #real Production

#img = Image.open('Screenshots/realScreen11.png')

#imgcropped = img.crop((706,230,1207,672)) # repl Production

# for realScreen
imgcropped = img.crop((1425,240,1884,660))

imgcropped.save('Screenshots/exampleProduction.png')
