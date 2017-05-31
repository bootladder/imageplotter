#!/usr/bin/python

#location2plotter.py

#This script takes in Parsed Sniffer Data
#and prepares it for plotting by imageplotter.py
#The Input Data is a CSV:  Location ID, String
#The Output Data is a CSV:  x,y,string

#This script takes 3 arguments:  Map, Input, Output
#The map is used to convert an ID to an X,Y coordinate

import argparse
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument("--map", help="CSV File in ID,x,y format")
parser.add_argument("--indata", help="CSV file in ID,String format")
parser.add_argument("--outdata", help="Output CSV File")
args = parser.parse_args()
if args.map and args.indata and args.outdata:
    print "location2plotter Starting.  Arguments: "
    print "map: %s , indata: %s , outdata: %s"%(args.map,args.indata,args.outdata)
else:
    print "FAIL!!!!"
    exit(0)

print "printing map"
with open(args.map, 'rb') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in csvreader:
         print row

print "convert map csv to dictionary"
with open(args.map, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    mydict = dict((  int(rows[0]) , ( int(rows[1]) , int(rows[2]) ) ) for rows in csvreader)
    print mydict

print "printing the input file"
with open(args.indata, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        print row

print "looping through the input file and writing to the output file"
with open(args.indata, 'rb') as csvfile:
 with open(args.outdata, 'w+') as outfile:

    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        #check payload
        if len(row) < 2 :
            continue
        coordinates = mydict.get( int(row[0]), None)
        outstring = '%d,%d,"%s"\n' %(coordinates[0],coordinates[1],row[1])
        print "outstring is" , outstring
        outfile.write(outstring)
    

print "DONE:  location2plotter"
