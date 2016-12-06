import os
import string
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
#
# This function reads the master input file which contains list of data files.
# It processes each data file to extract runners and his/her running distance.
# The extracted data are stored in lists and dictionaries which are processed
# to produce the required results.
#
# Notes:
# MN: you are relying on implicit global variables.
#     I would like you to not use the Globals and explicitly pass values back and for
#


# The master input file
# MN: why not asking the user for the master list file name?
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
            if os.path.isfile(data_file):
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
            if runner in runner_distance_dict:
                runner_distance_dict[runner] = distance + runner_distance_dict[runner]
            else:
                runner_distance_dict[runner] = distance

            # Update the runner appearance dictionary
            if runner in runner_records_dict:
                runner_records_dict[runner] = 1 + runner_records_dict[runner]
            else:
                runner_records_dict[runner] = 1
        except ValueError:
            pass

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

def main():
    ##################################
    # Process files
    ##################################

    if os.path.isfile(master_input_list_file):
        fh = open(master_input_list_file, 'r')
        processMasterFile(fh)
        fh.close

    ##################################
    # Process data
    ##################################

    # Total number of data files
    number_of_files = len(data_file_list)
    # Total number of lines
    total_number_of_lines = len(data_list)
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

    for runner, distance in runner_distance_dict.items():
        total_distance += distance
        total_number_of_runner += 1
        if distance > max_distance_run:
            max_distance_run = distance
            max_distance_runner = runner
        if distance < min_distance_run:
            min_distance_run = distance
            min_distance_runner = runner

    # MN: why not combining this loop with the previous one
    output_fh = open(output_file, 'w')
    for runner, records in runner_records_dict.items():
        distance = runner_distance_dict[runner]
        # output = '{0:s},{1:d},{2,.2f}'.format(runner, records, distance)
        output_fh.write('%s,%d,%.2f\n\r' % (runner, records, distance))
        if records > 1:
            number_of_runner_with_multiple_records += 1
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
