#!/bin/python
# Image Plotter
# Arguments:   Image, Data
# Data is a CSV, consists of x,y,string, and will be printed on the image.

import numpy as np
import cv2
import argparse
import csv 
import os 

parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image to be printed on")
parser.add_argument("--data", help="CSV file in x,y,string format")
parser.add_argument("--outimage", help="Output Image")
args = parser.parse_args()
if args.data and args.image and args.outimage:
    print "Image Plotter Starting.  Arguments: "
    print "data: %s , image: %s , output: %s"%(args.data,args.image,args.outimage)
else:
    print "FAIL!!!!"
    exit(0)


print "Reading image and data, and Drawing on image"

img = cv2.imread(args.image,cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_SIMPLEX

f = open(args.data)
reader = csv.reader(f)
for row in reader:
    print "x: ",int(row[0])," y: ",int(row[1])," data: ",row[2]
    cv2.putText(img,row[2],(int(row[0]),int(row[1])), font, 0.5,(255,55,55),2)
f.close()

print "writing output image"
cv2.imwrite( args.outimage, img);












#print outfilename + " is being printed"
#outfilename = os.path.splitext(os.path.basename(args.image))[0]  
#outfilename += "." +  os.path.splitext(os.path.basename(args.data))[0] + ".jpg"
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
