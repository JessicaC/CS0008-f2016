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

# The master input file
master_input_list_file = 'f2016_cs8_a3.data.txt'
# The output file that contains runners, records in data files and the total distance run
output_file = 'f2016_cs8_jzc22_a3.data.output.csv'
# List to store all data files (read from master input list)
data_file_list = []
# List to store all data read from all data files. Each element is pair (name, distance).
data_list = []
# Dictionary to store all runners and distances. The key is runner name, value is his/her total distance
runner_distance_dict = {}
# Dictionary to store all runners and record count
runner_records_dict = {}

# This function accepts one argument: the master input file handle.
# It reads all data files and process each data file.
def processMasterFile(fh):
    for line in fh:
        try:
            # Strip the \n to get data file name
            data_file = line.rstrip()

            # Add to data_file_list
            data_file_list.append(data_file)

            # Process the data file
            if (os.path.isfile(data_file)):
                data_fh = open(data_file, 'r')
                processDataFile(data_fh)
                data_fh.close
        except ValueError:
            pass

# This function accepts one argument: the data file handle.
# It reads data line by line to extract runner and his/her distance.
# Extracted data are stored into data_list and runner_distance_dict and runner_records_dict.
def processDataFile(fh):
    for line in fh:
        try:
            # Strip the \n
            line = line.rstrip()
            # Split the names and distances (string and float)
            stt = line.split(",")

            runner = stt[0].strip()  # strip to trim leading and trailing space
            distance = float(stt[1])

            # Append to data_list
            data_list.append((runner, distance))

            # Update the runner distance dictionary
            if (runner in runner_distance_dict):
                runner_distance_dict[runner] = distance + runner_distance_dict[runner]
            else:
                runner_distance_dict[runner] = distance

            # Update the runner appearance dictionary
            if (runner in runner_records_dict):
                runner_records_dict[runner] = 1 + runner_records_dict[runner]
            else:
                runner_records_dict[runner] = 1
        except ValueError:
            pass


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
