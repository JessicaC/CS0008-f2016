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
sys = input("Which system do you want to use, USC or Metric? ")
# Ask user for distance driven and how much gasoline was used; the units depend on the system selected by user
if sys == 'USC':
    miles = float(input("Number of miles driven: "))
    gallons = float(input("Gallons of gasoline used: "))
    km = miles * 1.60934
    liters = gallons * 3.78541
    print(format(miles, '.3f') + ' miles')
    print(format(gallons, '.3f') + ' gallons')
    print(format(km, ',.3f') + ' km')
    print(format(liters, '.3f') + ' liters')
elif sys == 'Metric':
    km = float(input("Number of km driven: "))
    liters = float(input("Liters of gasoline used: "))
    miles = km / 0.621371
    gallons = liters / 0.264172
    print(format(miles, '.3f') + ' miles')
    print(format(gallons, '.3f') + ' gallons')
    print(format(km, '.3f') + ' km')
    print(format(liters, '.3f') + ' liters')
mpg = miles / gallons
print(format(mpg, ',.3f') + ' mpg')
cm = 100 * liters / km
print (format(cm, '.3f') + ' 1/100km')