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
#
# Ask the user to enter the name of the text file. Loop indefinitely until the user enters 'quit', an empty string, or
# a 'q'
while file_name != 'quit' & '' & 'q':
    file_name = input("Enter the name of the text file: ")
def processFile(fh):
    data_1 = open('data_1.txt', 'r')
    data_2 = open('data_2.txt', 'r')

    numlines1 = 0
    numlines2 = 0
    for line in open('data_1.txt'): numlines1 += 1
    for line in open('data_2.txt'): numlines2 += 1

    name1 = data_1.readline()
    name2 = data_2.readline()

    while name1 != '':
        distance1 = data_1.readline()

        # Strip the newlines
        name1 = name1.rstrip('\n')
        distance1 = distance1.rstrip('\n')

    while name2 != '':
        distance2 = data_2.readline()

        name2 = name2.rstrip('\n')
        distance2 = distance2.rstript('\n')
    result1 = 0
    result2 = 0
    for line in open('data_1.txt'): result1 += int(line.strip())
    for line in open('data_2.txt'): result2 += int(line.strip())

    data_1.close()
    data_2.close()

    print("File to be read: data1.csv")
    print("Partial Total # of lines: ", numlines1)
    print("Partial distance run: ", result1)

    print("File to be read: data2.csv")
    print("Partial Total # of lines: ", numlines2)
    print("Partial distance run: ", result2)

    print("File to be read: quit")

    print("Totals")
    print("Total # of lines: ", numlines1 + numlines2)
    print("Total distance run: ", result1 + result2)


processFile()
