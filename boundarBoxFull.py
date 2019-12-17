import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

# listedeki img ve txt'leri oku. 
# tzt içindeki değerleri her fotoğraf için ayır

def takePathOfFiles(imgPathFile):
    k = 0
    for imagePath in imgPathFile:
        imagePath = imagePath.split("\n")
        imagePath = imagePath[0]
        im        = Image.open(imagePath)
        
        x, y, w, h     = changePath(imagePath)
        
        width, height  = im.size
        img            = np.array(im, dtype = np.uint8)
        
        #print("image size : %1, %2") #format ile ekrana yazdır. 
        
        x1, y1, W, H = getPointData(x,y,w,h,width,height)
        
        fig, ax      = plt.subplots(1)
        ax.imshow(img)
        rect = patches.Rectangle( (x1, y1), W, H, linewidth=1,edgecolor='r',facecolor='none', alpha=1)
        ax.add_patch(rect)
        distFilename = "/home/sam/Desktop/boundaryBoxOnImage/drawedImages" + str(k)
        k = k + 1
        fig.savefig(distFilename, transparent=True)#, bbox_inches='tight', pad_inches=0, dpi=150)
        print(k -1)

def changePath(path):
    newPath = path.split("images")
    newPath = newPath[0] + "labels" + newPath[1]
    newPath = newPath.split("jpg")
    newPath = newPath[0] + "txt"
    print(newPath)
    txtFile = open(newPath,"r")
    for line in txtFile:
        line = line.split(" ")
        x_ = line[1]
        y_ = line[2]
        w_ = line[3]
        h_ = line[4]

    return x_, y_, w_, h_


def getPointData(x, y, w, h, width, height):
    
    x2 = (float(w) * (2 * float(x) + float(width))) / 2
    x1 = 2 * float(w) * float(x) - x2

    y2 = (float(h) * (2 * float(y) + float(height))) / 2
    y1 = 2 * float(h) * float(y) - y2

    newW = abs(x2 - x1)
    newH = abs(y2 - y1)
    return x1, y1, newW, newH

#txtFile = open("/home/sam/Desktop/boundaryBoxOnImage/newlistOfLabelPath.txt","r")
imgFile = open("/home/sam/Desktop/boundaryBoxOnImage/newlistOfImagePath.txt","r")

takePathOfFiles(imgFile)
imgFile.close()