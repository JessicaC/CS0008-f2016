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
# A customer needs to process a number of text files that countain names and distance run by study participants.
#
# Open and read each data files
data1 = open('f2016_cs8_a3.data.1.csv', 'r')
data2 = open('f2016_cs8_a3.data.2.csv', 'r')
data3 = open('f2016_cs8_a3.data.3.csv', 'r')

# Total number of lines read

# Total Distance run

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
print("Total number of lines read: ")
print("")
print("total distance run: ")
print("")
print("max distance run: ")
print("by participant: ")
print("min distance run: ")
print("by participant: ")
print("")
print("Total number of participants: ")
print("Number of participants")
print("with multiple records: ")
