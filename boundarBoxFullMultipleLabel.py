import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os

def takePathOfFiles(imgPathFile):
    
    for imagePath in imgPathFile:
        imagePath = imagePath.split("\n")
        imagePath = imagePath[0]

        #####################################################
                
        newPath = imagePath.split("images")
        newPath = newPath[0] + "labels" + newPath[1]
        newPath = newPath.split("jpg")
        newPath = newPath[0] + "txt"
#        print(newPath)

        if os.stat(newPath).st_size == 0:
            #print("File is Empty")
            #c_ = 0; x_ = 0;  y_ = 0;  w_ = 0;  h_ = 0
            continue
        else:
            im        = Image.open(imagePath)
            width, height  = im.size
            img            = np.array(im, dtype = np.uint8)

            fig, ax      = plt.subplots(1)
            ax.imshow(img)
            
            txtFile = open(newPath,"r")
 #           print(txtFile)
            for line in txtFile:
                line = line.split(" ")
                c = line[0]
                x = line[1]
                y = line[2]
                w = line[3]
                h = line[4]

                c = checkClassification(c)
            
                x1, y1, W, H = getPointData(x,y,w,h,width,height)


                rect = patches.Rectangle( (x1, y1), W, H, linewidth=1, edgecolor=c, facecolor='none', alpha=1)

                ax.add_patch(rect)
            
            distFilename = checkForDistanceFolder(imagePath)
        
        
            fig.savefig(distFilename, transparent=True)#, bbox_inches='tight', pad_inches=0, dpi=150)
        
        
         



        ##############################################
#        c, x, y, w, h  = changePath(imagePath)
#        
#        
#        if w == 0 and h == 0:
#            continue 
#        width, height  = im.size
#        img            = np.array(im, dtype = np.uint8)
#
#
#        x1, y1, W, H = getPointData(x,y,w,h,width,height)
#        
#        fig, ax      = plt.subplots(1)
#        
#        ax.imshow(img)
#        
#
#        rect = patches.Rectangle( (x1, y1), W, H, linewidth=1, edgecolor=c, facecolor='none', alpha=1)
#        
#        ax.add_patch(rect)
#        #checkForDistanceFolder(imagePath)
#        distFilename = checkForDistanceFolder(imagePath)
#        
#        
#        fig.savefig(distFilename, transparent=True)#, bbox_inches='tight', pad_inches=0, dpi=150)
        

def checkForDistanceFolder(imgPath):
    
    #print(imgPath)
    folderPath = imgPath
    folderPath = folderPath.split("CTU/newSubt/")
    folderPath = folderPath[0] + folderPath[1]

    distFile   = folderPath
    folderPath = folderPath.split("/frame")
    folderPath = folderPath[0]
    print(folderPath)
    #print(distFile)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    
    return distFile


def changePath(path):
    
 
    newPath = path.split("images")
    newPath = newPath[0] + "labels" + newPath[1]
    newPath = newPath.split("jpg")
    newPath = newPath[0] + "txt"
#    print(newPath)

    if os.stat(newPath).st_size == 0:
        #print("File is Empty")
        c_ = 0; x_ = 0;  y_ = 0;  w_ = 0;  h_ = 0
        return c_, x_, y_, w_, h_
    else:
        txtFile = open(newPath,"r")
 #       print(txtFile)
        for line in txtFile:
            line = line.split(" ")
            c_ = line[0]
            x_ = line[1]
            y_ = line[2]
            w_ = line[3]
            h_ = line[4]

        c_ = checkClassification(c_)

        return c_, x_, y_, w_, h_










def checkClassification(classname):
    if classname == "0":
        classColor = 'r'
    elif classname == "1":
        classColor = 'g'
    elif classname == "2":
        classColor = 'b'
    elif classname == "3":
        classColor = 'c'

    return classColor

def getPointData(x, y, w, h, width, height):
    
    x2 = float(width) * (2 * float(x) + float(w)) / 2

    x1 = x2 - width * float(w)

    y2 = float(height) * (2 * float(y) + float(h)) / 2
    y1 = y2 - height * float(h)

    newW = abs(x2 - x1)
    newH = abs(y2 - y1)

    return x1, y1, newW, newH

#txtFile = open("/home/sam/Desktop/boundaryBoxOnImage/newlistOfLabelPath.txt","r")
imgFile = open("/home/samy/Desktop/boundaryBoxOnImage/newlistOfImagePath2.txt","r")

takePathOfFiles(imgFile)
imgFile.close()