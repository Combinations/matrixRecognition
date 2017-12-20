# using the mnist data set generate arrays of images representing a hand written matrix
from __future__ import print_function
from PIL import Image
im1 = Image.open("./mnist/train-images/3697.jpg")
im2 = Image.open("./mnist/train-images/3698.jpg")
im3 = Image.open("./mnist/train-images/3699.jpg")
im4 = Image.open("./mnist/train-images/3400.jpg")

reg1 = (0, 0, 28, 28)
reg2 = (28,28,56,56) 
reg3 = (0, 28, 28, 56)
reg4 = (28, 0, 56, 28)

newImage = Image.new("L", (56,56), "white")
newImage.paste(im1, reg1)
newImage.paste(im2, reg2)
newImage.paste(im3, reg3)
newImage.paste(im4, reg4)
print(newImage.format, newImage.size, newImage.mode)
newImage.save("new.jpeg")


