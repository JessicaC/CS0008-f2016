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

def printkv (key, value, klen=0):
    kn = len(key)
    space = klen
    # Get the max space
    if kn > klen:
        space = kn

    # Is the value int?
    if isinstance(value,int):
        print("%20s : %10d" %(key, value))
    else:
        print("%20s : %10.3f"%(key,value))

whole_lines = 0
whole_total = 0

while True:
    fh = input("File to be read: ")
    if(fh == "quit") or (fh == "q") or (fh == ""):
        break;
    linecount, sumtotal = processfile(fh)

    printkv('Partial Total # of lines ', linecount,20)
    printkv('Partial distance run', sumtotal)
    whole_lines += linecount
    whole_total += sumtotal

print("Totals")
printkv('Total # of lines ',whole_lines,20)
printkv('Total distance run',whole_total)