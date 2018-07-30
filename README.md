# GoogleDinoBot
A bot to play google's offline mode dino game

A few lines of code will have to be changed according to your screen size

1. The coordinates of the replay button
2. BOX, a small region in front of the dino in which if a tree enters the dino jumps (find the optimum area by trial and error)
3. 3447 is the value of sum of greyscale pixels of the box when it is grey and there is no tree, as soon as a tree enters the box the values change and the condition becomes true and it jumps. Find the sum of your area when it is blank by printing out the imageGrab() function
