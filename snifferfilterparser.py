#!/usr/bin/python

#snifferfilterparser.py

#This script takes in raw data from the sniffer
#Filters out unwanted packets, based on their payload
#Then extracts a location ID from the payload
#And creates a string to be displayed or plotted

#The Raw Data is a CSV:  timestamp, data ID, rssi, LQI, num messages
#The output is a CSV:  ID,string

#This script takes 2 arguments:  Input Data, Output Data

import argparse
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument("--indata", help="CSV file in timestamp,channel,rssi,LQI,payload format")
parser.add_argument("--outdata", help="Output  Parsed CSV File")
args = parser.parse_args()
if args.indata and args.outdata:
    print "snifferfilterparser Starting.  Arguments: "
    print "indata: %s , outdata: %s"%(args.indata,args.outdata)
else:
    print "FAIL!!!!"
    exit(0)


print "printing the input data"
with open(args.indata, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        print row

print "looping through the input data"
with open(args.indata, 'rb') as csvfile:
  with open(args.outdata, 'w+') as outfile:
  
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #csvwriter = csv.writer(outfile, delimiter=',')
    rownum=0
    for row in csvreader:
        #check payload
        if len(row) < 4 :
            continue
        elif "BEEF" not in row[4]:
            print "FILTERED:  " , row[4]
        else :
            print "ACCEPTED:  " , row[4]
            locationID = int( row[4][32:34],16) 
            print "Location ID: %d" %( locationID )
            print "RSSI: %d" %(int(row[2]))
            print "LQI: %d" %(int(row[3]))
            rowstring = '%d,%d,%d\n' %(locationID   , int(row[2]) , int(row[3]) )
            print rowstring
            outfile.write(rowstring)

print "DONE:  snifferfilterparser"
