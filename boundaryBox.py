import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import cv2 as cv

#
#
im = Image.open('/home/sam/Desktop/boundaryBoxOnImage/frame000229.jpg')
txt = open('/home/sam/Desktop/boundaryBoxOnImage/frame000229.txt','r')

for line in txt:
    strTxt = line.split(' ')

print(strTxt[2])
width, height = im.size

print(width)
print(height)


im = np.array(im, dtype=np.uint8)


# Create figure and axes
fig,ax = plt.subplots(figsize = (width/100,height/100))

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((668.666,269.6507),49.968,146.8563,linewidth=1,edgecolor='r',facecolor='none', alpha=1)

# Add the patch to the Axes
ax.add_patch(rect)
fig.savefig("/home/sam/Desktop/boundaryBoxOnImage/tes2t.jpg", transparent=True, bbox_inches='tight', pad_inches=0)#, dpi=150)

plt.show()
