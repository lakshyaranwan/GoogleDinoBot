from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class cordinates:
    #the coordinates of the replay button of the game, depending on your screen size
    replayBtn = (360,240)

def restartGame():
    pyautogui.click(cordinates.replayBtn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.01)
    pyautogui.keyUp('space')

def imageGrab():
    #the coordinates of a square in front of the dino, when a tree enters the box, the dino jumps
    #x1,y1 top left corner ; x2,y2 bottom right corner
    box = (150,242,250,274)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    return (a.sum())

restartGame()
while True:
    print(imageGrab())
    #3447 is the value of the sum of the pixels greyscale values of the box when there is no tree
    if(imageGrab()!=3447):
        jump()





