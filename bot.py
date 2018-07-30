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

def imageGrab():
    box = (150,242,250,274)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    return (a.sum())

restartGame()
while True:
    print(imageGrab())
    if(imageGrab()!=3447):
        jump()





