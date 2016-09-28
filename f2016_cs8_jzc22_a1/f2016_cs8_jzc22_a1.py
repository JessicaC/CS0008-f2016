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
distance = float(input("Distance driven: "))
gasoline = float(input("Gasoline used: "))
if sys == 'USC':
    distance_units = 'miles'
    gasoline_units = 'gallons'
    print(format(distance, '6.3f') + distance_units)
    print(format(gasoline, '6.3f') + gasoline_units)
elif sys == 'Metric':
    distance_units = 'km'
    gasoline_units = 'liters'
    print(format(distance, '6.3f') + distance_units)
    print(format(gasoline, '6.3f') + gasoline_units)
# Consumption rating
cm = 100 * gasoline / distance
cm1 = 20
cm2 = 15
cm3 = 10
cm4 = 8
if cm > cm1:
    rating = 'Extremely Poor'
elif cm >= cm2:
    rating = 'Poor'
elif cm >= cm3:
    rating = 'Average'
elif cm >= cm4:
    rating = 'Good'
elif cm <= cm4:
    rating = 'Excellent'

print('\t\t\t\t\t\tUSC\t\tMetric')
print('Distance\t\t: ')
print('Gas\t\t\t\t: ')
print('Consumption\t\t: ')
print('Gas consumption rating: ' + rating, sep='')
