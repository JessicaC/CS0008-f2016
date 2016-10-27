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
def processfile(fh):
    # Count the number of lines in the text file
    linecount = 0

    # Sum up the values in the text file
    sumtotal = 0

    # Open the file
    fid = open(fh, 'r')

    # Count number of lines in files
    for line in fid:
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
def printkv (key, value, klen=0):
    kn = len(key)
    space = klen
    # Get the max space
    if kn > klen:
        space = kn

    # Format of value changes according to the type of the value contained in the variable
    if isinstance(value,int):
        print("%20s : %10d" %(key, value))
    else:
        print("%20s : %10.3f"%(key,value))
# Add up the total lines and total distance run for both files to get an overall total
whole_lines = 0
whole_total = 0

while True:
    fh = input("File to be read: ")
    if(fh == "quit") or (fh == "q") or (fh == ""):
        break;
    linecount, sumtotal = processfile(fh)

# Print out the output
    printkv('Partial Total # of lines ', linecount,20)
    printkv('Partial distance run', sumtotal)
    whole_lines += linecount
    whole_total += sumtotal

print("Totals")
printkv('Total # of lines ',whole_lines,20)
printkv('Total distance run',whole_total)