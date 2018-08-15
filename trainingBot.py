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


decrease = 50
restartGame()
x2 = 245
dist = 0
bestRun = 0
while True:
    if(imageGrab(345,230,375,250)==930):
        x2=245
        print("----------------------------------Decrease:")
        print(decrease)
        print("----------------------------------Dist:")
        print(dist)
        if(dist>bestRun):
            max = decrease
            bestRun = dist
        print("----------------------------------Best Reduce:")
        print(max)
        count = 0
        decrease = decrease+1
        restartGame()
    else:
        dist = dist+10
        x2 = x2+(1/decrease)
        print(x2)
        jumpValue = imageGrab(150, 150, x2, 182)
        if(imageGrab(150,242,x2,274)!=jumpValue):
            jump()



#old Code
# from PIL import ImageGrab, ImageOps
# import pyautogui
# import time
# from numpy import *

# class cordinates:
   
#     replayBtn = (360,240)

# def restartGame():
#     pyautogui.click(cordinates.replayBtn)

# def jump():
#     pyautogui.keyDown('space')
#     time.sleep(0.01)
#     pyautogui.keyUp('space')

# def imageGrab():
#     #the coordinates of a square in front of the dino, when a tree enters the box, the dino jumps
#     #x1,y1 top left corner ; x2,y2 bottom right corner
#     box = (150,242,250,274)
#     image = ImageGrab.grab(box)
#     greyImage = ImageOps.grayscale(image)
#     a = array(greyImage.getcolors())
#     return (a.sum())

# restartGame()
# while True:
#     print(imageGrab())
#     #3447 is the value of the sum of the pixels greyscale values of the box when there is no tree
#     if(imageGrab()!=3447):
#         jump()

        












