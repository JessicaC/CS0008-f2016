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
def processFile(lines1, lines2, result1, result2):
    # Ask the user to enter the name of the text file. Loop indefinitely until the user enters 'quit', an empty string,
    # or a 'q'
    while file_name != 'quit' or '' or 'q':
        file_name = input("Enter the name of the text file: ")

    data_1 = open('data_1.txt', 'r')
    data_2 = open('data_2.txt', 'r')

    lines1 = 0
    lines2 = 0
    if file_name == 'data_1.txt':
        for line1 in open('data_1.txt'):
            lines1 += 1
    elif file_name == 'data_2.txt':
        for line2 in open('data_2.txt'):
            lines2 += 1

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
        distance2 = distance2.rstrip('\n')
    # Sum up the values
    result1 = 0
    result2 = 0
    for line in open('data_1.txt'):
        amount1 = float(line)
        result1 += amount1
    for line in open('data_2.txt'):
        amount2 = float(line)
        result2 += amount2

    data_1.close()
    data_2.close()

    print("File to be read: data1.csv")
    print("Partial Total # of lines: ", lines1)
    print("Partial distance run: ", result1)

    print("File to be read: data2.csv")
    print("Partial Total # of lines: ", lines2)
    print("Partial distance run: ", result2)

    print("File to be read: quit")

    print("Totals")
    print("Total # of lines: ", lines1 + lines2)
    print("Total distance run: ", result1 + result2)


processFile()

def printkv(key, value, klen=0):
    print("blah")