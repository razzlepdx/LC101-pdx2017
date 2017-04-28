# Studio for class Apr27
# write an algorithm that processes an image to make it “fuzzy” looking:
# for each pixel, randomly choose one of its neighbor pixels, and use the neighbor’s color instead.
###################

import image
import sys
import random

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):

        # TODO: Randomly choose the coordinates of a neighboring pixel
        random_i = random.randint(i-1, i+1)
        random_j = random.randint(j-1, j+1)

        # TODO: in the new image, set this pixel's color to the neighbor's color
        random_coordinates = img.getPixel(random_i,random_j)
        newimg.setPixel(i,j, random_coordinates)

newimg.draw(win)
win.exitonclick()

######################
