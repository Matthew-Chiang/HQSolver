import os
import time
from PIL import Image
import numpy

def savePic(image):
    ts = time.gmtime()
    timeStamp = time.strftime("%Y-%m-%d", ts)
    #print(timeStamp)

    hour = int(time.strftime("%H",ts))

    if hour in range(18,20): # these hours are in UTC - range of 2-3 EST
        directory = "Results/Pics/" + timeStamp + "/3PM"

    elif hour in range(0,2):
        directory = "Results/Pics/" + timeStamp + "/9PM"
    else:
        directory = "Results/Pics"


    if os.path.isdir(directory):
        savePath = directory + "/" + str(len(os.listdir(directory))) + ".png"
        image.save(savePath)
    else:
        os.makedirs(directory)
        savePath = directory + "/" + str(   len(os.listdir(directory))) + ".png"
        image.save(savePath)
