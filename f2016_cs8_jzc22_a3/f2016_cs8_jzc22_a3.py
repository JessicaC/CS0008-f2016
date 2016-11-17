#
#
# name          : Jessica Chen
# email         : jzc22@pitt.edu
# date          : 11/15/2016
# class         : CS0008-f2016
# instructor    : Max Novelli
#
# Description:
# Assignment 3
# A customer needs to process a number of text files that contain names and distance run by study participants.
#
# Open and read each data files
data1 = open('f2016_cs8_a3.data.1.csv', 'r')
data2 = open('f2016_cs8_a3.data.2.csv', 'r')
data3 = open('f2016_cs8_a3.data.3.csv', 'r')

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

totallines =  linecount1 + linecount2 + linecount3


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
