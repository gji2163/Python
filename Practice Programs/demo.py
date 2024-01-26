import numpy as np
import glob
import cv2
import video

img_array=[]

for filename in glob.glob(input("Enter image name:")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    for i in range(15*int(input("Length:"))):
        img_array.append(img)
 



out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
 
video.play('project.avi')

