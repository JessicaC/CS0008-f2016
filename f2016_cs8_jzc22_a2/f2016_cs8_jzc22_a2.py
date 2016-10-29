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
# Assignment 2
#
# This function accepts one argument in input that is the handle to the file object to be read. Returns two values,
# how many lines the file has and the total sum of the distance of each record
import string


def processFile(fh):
    # Count the number of lines in the text file
    linecount = 0

    # Sum up the values in the text file
    sumtotal = 0

    # Count number of lines in files
    for line in fh:
        linecount += 1
        # Strip the \n
        line = line.rstrip()
        # Split the names and distances (string and float)
        stt = line.split(",")
        # Sum up the values
        sumtotal += float(stt[1])

    return linecount, sumtotal


# This function accepts 2 mandatory arguments: key and value and an optional third klen (key length). If klen is not
# passed when called, it defaults to 0
def printKV(key, value, klen=0):
    kn = len(key)
    space = klen
    # Get the max space for key
    if kn > klen:
        space = kn

    # Format of value changes according to the type of the value contained in the variable
    value_str = ''
    if isinstance(value, int):
        value_str = format(value, '10d')
    elif isinstance(value, float):
        value_str = format(value, '10.3f')
    else:
        value_str = format(value, '30s')

    format_str = '{0:' + str(space) + 's} : {1:s}'
    print(format_str.format(key, value_str))


# Add up the total lines and total distance run for both files to get an overall total
whole_lines = 0
whole_total = 0
klen = 30
while True:
    fname = input("File to be read: ")
    if (fname == "quit") or (fname == "q") or (fname == ""):
        break;

    # check file existence
    if (os.path.isfile(fname)):
        fh = open(fname, 'r')
        linecount, sumtotal = processFile(fh)
        fh.close

        # Print out the output
        printKV('File read', fname, klen)
        printKV('Partial Total # of lines', linecount, klen)
        printKV('Partial distance run', sumtotal, klen)
        whole_lines += linecount
        whole_total += sumtotal

print("Totals")
printKV('Total # of lines ', whole_lines, klen)
printKV('Total distance run', whole_total, klen)