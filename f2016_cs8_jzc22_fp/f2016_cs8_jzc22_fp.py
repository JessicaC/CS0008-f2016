import os
import string
#
#
# name          : Jessica Chen
# email         : jzc22@pitt.edu
# date          : 12/5/2016
# class         : CS0008-f2016
# instructor    : Max Novelli
#
# Description:
# Final Project
#
# This program reads the master input file which contains list of data files.
# It processes each data file to extract runners and his/her running distance.
# The extracted data are stored in lists and dictionaries which are processed
# to produce the required results.

# Defines a participant.
class participant:

    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
        else:
            # set distance
            self.distance = 0
            # set number of runs
            self.runs = 0

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            # end if

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                # end if
                # end for

    # Get name of participant
    def getName(self):
        return self.name

    # Get total distance run
    def getDistance(self):
        return self.distance

    # Get number of runs
    def getRuns(self):
        return self.runs

    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

# This function accepts one argument: the master input file handle.
# It reads all data files and process each data file.
# Data file processed will be stored in data_file_list.
# Information read from data files will be stored in participants_dict.
#
# Arguments:
# fh - master file handle
# data_file_list - list to store data file names.
# participants_dict - name to participant dictionary.
def processMasterFile(fh, data_file_list, participants_dict):
    for line in fh:
        try:
            # Strip the \n to get data file name
            data_file = line.rstrip()

            # Add to data_file_list
            data_file_list.append(data_file)

            # Process the data file
            if os.path.isfile(data_file):
                data_fh = open(data_file, 'r')
                processDataFile(data_fh, participants_dict)
                data_fh.close
        except ValueError:
            pass

# This function reads data line by line from a file to extract
# runner name and his/her distance. Extracted data are used to update
# the participants_dict.
#
# Arguments:
#   fh - the data file handle
#   participants_dict - name to participant dictionary.
def processDataFile(fh, participants_dict):
    for line in fh:
        try:
            # Strip the \n
            line = line.rstrip()
            # Split the names and distances (string and float)
            stt = line.split(",")

            name = stt[0].strip()  # strip to trim leading and trailing space
            distance = float(stt[1])

            # Update the participant dictionary
            if name in participants_dict:
                participants_dict[name].addDistance(distance)
            else:
                participants_dict[name] = participant(name, distance)

        except ValueError:
            pass

# This function accepts 2 mandatory arguments: key and value and an optional third klen (key length). If klen is not
# passed when called, it defaults to 0. It prints the key and value with desired format.
#
# Arguments:
# key - key string.
# value - value object, this can be int, float, string.
# klen - optional key length, default is 0.
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

def main():
    # The master input file
    master_input_list_file = 'f2016_cs8_fp.data.txt'
    # The output file that contains runners, records in data files and the total distance run
    output_file = 'f2016_cs8_jzc22_fp.data.output.csv'
    # List to store all data files (read from master input list)
    data_file_list = []
    # Map from name to participant object
    participants_dict = {}

    ##################################
    # Process files
    ##################################

    if os.path.isfile(master_input_list_file):
        fh = open(master_input_list_file, 'r')
        processMasterFile(fh, data_file_list, participants_dict)
        fh.close

    ##################################
    # Process data
    ##################################

    # Total number of data files
    number_of_files = len(data_file_list)
    # Total number of lines
    total_number_of_lines = 0
    # Total number of runners
    total_number_of_runner = 0
    # Total distance run by all runners
    total_distance = 0.0
    # Max distance run by a runner
    max_distance_run = 0.0
    # The runner with max distance
    max_distance_runner = ''
    # Min distance run by a runner
    min_distance_run = 9999999.0
    # The runner with min distance
    min_distance_runner = ''
    # The number of runners with multiple records
    number_of_runner_with_multiple_records = 0

    output_fh = open(output_file, 'w')

    for runner, participant in participants_dict.items():
        distance = participant.getDistance()
        runs = participant.getRuns()
        total_distance += distance
        total_number_of_lines += runs
        total_number_of_runner += 1
        if distance > max_distance_run:
            max_distance_run = distance
            max_distance_runner = runner
        if distance < min_distance_run:
            min_distance_run = distance
            min_distance_runner = runner
        if runs > 1:
            number_of_runner_with_multiple_records += 1

        output_fh.write(participant.tocsv() + "\n\r")

    output_fh.close()

    ##################################
    # Print results
    ##################################

    klen = 30
    # Print out the number of input files
    printKV('Number of Input files read', number_of_files, klen)

    # Print out total number of lines read
    printKV('Total number of lines read', total_number_of_lines, klen)
    print('')

    # Print out total distance run
    printKV('total distance run', total_distance, klen)
    print('')

    printKV('max distance run', max_distance_run, klen)
    printKV('by participant', max_distance_runner, klen)
    print('')

    printKV('min distance run', min_distance_run, klen)
    printKV('by participant', min_distance_runner, klen)
    print('')

    printKV('Total number of participants', total_number_of_runner, klen)
    print('')

    print('Total number of participants ')
    printKV('with multiple records', number_of_runner_with_multiple_records, klen)
    print('')

# use the main() function
main()
