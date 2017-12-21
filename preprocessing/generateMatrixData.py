# using the mnist data set generate arrays of images representing a hand written matrix
from __future__ import print_function
from PIL import Image
import csv

labels = open("./mnist/train-labels.csv", "rb")
newLabels = open("./mnist/matrix-train-labels.csv", "wb")
reader = csv.reader(labels)
labelWriter = csv.writer(newLabels)

def imagePosition(x):
    return {
        1: (0,0,28,28),
        2: (28,0,56,28),
        3: (0,28,28,56),
        4: (28,28,56,56)
}[x]

newImage = Image.new("L", (56,56), "white")

imageCounter = 1;
generated = 1;
newLabel = []

for row in reader:
    i = Image.open("./mnist/" + row[0])
    newImage.paste(i, imagePosition(imageCounter))
    newLabel.append(row[1])
    if(imageCounter == 4): 
        imageCounter = 1;
        imageName = "matrix" + str(generated) + ".jpg"
        newImage.save("./mnist/matrix-train-images/" + imageName)
        labelWriter.writerow([imageName, newLabel[0], newLabel[1], newLabel[2], newLabel[3]])
        print(newLabel)
        newLabel = []
        generated = generated + 1;
    else: 
        imageCounter = imageCounter + 1 

















