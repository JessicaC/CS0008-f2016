import os
#
#
# name          : Jessica Chen
# email         : jzc22@pitt.edu
# date          : 10/25/2016
# class         : CS0008-f2016
# instructor    : Max Novelli
#
# Description:
# Assignment 3
#
# This function reads the master input file which contains list of data files.
# It processes each data file to extract runners and his/her running distance.
# The extracted data are stored in lists and dictionaries which are processed
# to produce the required results.
import string

with open('data1.txt', 'r') as in_file:
    data1 = in_file.read().split('\n')
with open('data2.txt', 'r') as in_file:
    data2 = in_file.read().split('\n')
with open('data3.txt', 'r') as in_file:
    data3 = in_file.read().split('\n')

# Total number of lines read
linecount1 = 0
linecount2 = 0
linecount3 = 0

for line in data1:
    linecount1 += 1
    # Strip the \n
    line = line.rstrip()
    # Split the names and distances (string and float)
    stt = line.split(",")

for line in data2:
    linecount2 += 1
    # Strip the \n
    line = line.rstrip()
    # Split the names and distances (string and float)
    stt = line.split(",")

for line in data3:
    linecount3 += 1
    # Strip the \n
    line = line.rstrip()
    # Split the names and distances (string and float)
    stt = line.split(",")

totallines = linecount1 + linecount2 + linecount3


# Total Distance run
subtotal1 = 0
subtotal2 = 0
subtotal3 = 0
try:
    subtotal1 += float(stt[1])
except ValueError:
    pass

try:
    subtotal2 += float(stt[1])
except ValueError:
    pass

try:
    subtotal3 += float(stt[1])
except ValueError:
    pass

totaldis = subtotal1 + subtotal2 + subtotal3

# Total distance run for each individual participant

# Close the files
data1.close()
data2.close()
data3.close()

# Create a list of the data files
flist = [data1, data2, data3]
# Get number of files
nfiles = len(flist)


print("Number of Input files read: " + nfiles)
print("Total number of lines read: " + totallines)
print("")
print("total distance run: " + totaldis)
print("")
print("max distance run: " + max(flist))
print("by participant: ")
print("min distance run: " + min(flist))
print("by participant: ")
print("")
print("Total number of participants: ")
print("Number of participants")
print("with multiple records: ")
