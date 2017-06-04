#!/usr/bin/python

#aggregatoranalyzer.py

#This script takes in PARSED DATA
#aggregates and analyzes the data
#And creates a string to be displayed or plotted

#The Parsed Data is a CSV:  data ID, rssi, LQI
#The output is a CSV:  ID,string
#One output line per string to be plotted on an image.

#This script takes 2 arguments:  Input Data, Output Data

import argparse
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument("--indata", help="CSV file in ID,rssi,LQI format")
parser.add_argument("--outdata", help="Output  Aggregated CSV File in ID,string format")
args = parser.parse_args()
if args.indata and args.outdata:
    print "aggregatoranalyzer Starting.  Arguments: "
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

    current_id_num = 0
    num_rows_with_id = 0
    analyzer_row_list = [0,0,0]
    mintracker = 0

    for row in csvreader:
        #check payload
        if len(row) < 2 :
            continue

        if int(row[0]) == current_id_num :
            #keep aggregating
            print "SAME ROW" , row
            row_rssi = int(row[1])
            num_rows_with_id += 1
            analyzer_row_list[1] += row_rssi

            if row_rssi < mintracker :
                mintracker = row_rssi

            print "NEW TEMPROW CONTENTS" , analyzer_row_list

        else :
            print "ANALYZING ROW: num rows: " , num_rows_with_id
            #analyze last ID num
            analyzer_row_list[0] = current_id_num
            if num_rows_with_id > 0:
                analyzer_row_list[1] = analyzer_row_list[1] / num_rows_with_id

            mindiff = analyzer_row_list[1] - mintracker

            analyzer_row_list[2] = mintracker
            print "END OF ID STREAM.  ANALYZED ROW: " , analyzer_row_list
            rowstring = '%d,"%d,%d"\n' %(analyzer_row_list[0], analyzer_row_list[1] , analyzer_row_list[2] )
            print rowstring
            outfile.write(rowstring)


            current_id_num = int(row[0])
            num_rows_with_id  = 1
            analyzer_row_list = [0,int(row[1]),0]
            mintracker = 0
            print "NEW ROW" , row


    print "FINAL ANALYZING ROW: num rows: " , num_rows_with_id
    #analyze last ID num
    analyzer_row_list[0] = current_id_num
    if num_rows_with_id > 0:
        analyzer_row_list[1] = analyzer_row_list[1] / num_rows_with_id

    mindiff = analyzer_row_list[1] - mintracker

    analyzer_row_list[2] = mintracker
    print "END OF ID STREAM.  ANALYZED ROW: " , analyzer_row_list
    rowstring = '%d,"%d,%d"\n' %(analyzer_row_list[0], analyzer_row_list[1] , analyzer_row_list[2] )
    print rowstring
    outfile.write(rowstring)


print "DONE:  aggregatoranalyzer"
