#actual bot

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class cordinates:
    replayBtn = (360,240)

def restartGame():
    pyautogui.click(cordinates.replayBtn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    pyautogui.keyUp('space')

def imageGrab(x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    return (a.sum())

def imageShow(x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    image = ImageGrab.grab(box)
    image.show()


decrease = 50   #insert trained value here for best runs
restartGame()
x2 = 245
while True:
        x2 = x2+(1/decrease)
        jumpValue = imageGrab(150, 150, x2, 182)
        if(imageGrab(150,242,x2,274)!=jumpValue):
            jump()







