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
#
#
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
if sys == 'USC':
    newdis = distance * 1.60934
    newgas = gasoline * 3.78541
    print(newdis + 'km')
    print(newgas + 'liters')
elif sys == 'Metric':
    newdis = distance / 0.621371
    newgas = gasoline / 0.264172
    print(newdis + 'miles')
    print(newgas + 'gallons')
# Compute the fuel consumption