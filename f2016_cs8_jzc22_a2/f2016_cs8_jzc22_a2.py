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
# Ask the user to enter the name of the text file. Loop indefinitely until the user enters 'quit', an empty string, or
# a 'q'
while file_name != 'quit' & '' & 'q':
    file_name = input("Enter the name of the text file: ")
def processFile(fh):
    data_1 = open('f2016_cs8_a2.data1.csv', 'r')
    data_2 = open('f2016_cs8_a2.data2.csv', 'r')

    count1 = len(data_1.readline())
    count2 = len(data_2.readline())

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


    data_1.close()
    data_2.close()


processFile()

print("File to be read: data1.csv")
print("Partial Total # of lines: ")
print("Partial distance run: ")

print("File to be read: data2.csv")
print("Partial Total # of lines: ")
print("Partial distance run: ")

print("File to be read: quit")

print("Totals")
print("Total # of lines: ")
print("Total distance run: ")