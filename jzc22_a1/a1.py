#
#
# name          : Jessica Chen
# email         : jzc22@pitt.edu
# date          : 09/27/2016
# class         : CS0008-f2016
# instructor    : Max Novelli
#
# Description:
# Assignment 1
#
# Prompts the user which system he/she wants to use
sys = input("Which system do you want to use, USC or Metric?")
# Ask user for distance driven and how much gasoline was used; the units depend on the system selected by user
distance = input("Distance driven: ")
gasoline = input("Gasoline used: ")
# Print the amounts
if sys == 'USC':
    print(distance + "miles")
elif sys == 'Metric':
    print(distance + "km")
# Convert the quantities