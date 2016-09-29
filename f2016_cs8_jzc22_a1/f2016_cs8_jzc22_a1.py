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
elif sys == 'Metric':
    km = float(input("Number of km driven: "))
    liters = float(input("Liters of gasoline used: "))
    miles = km / 0.621371
    gallons = liters / 0.264172
# Fuel consumption
mpg = miles / gallons
# Consumption rating
cm = 100 * liters / km
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
# Output
print('\t\t\t\t\tUSC\t\t\t\t\tMetric')
print('Distance\t: ' + format(miles, '8.3f') + ' miles\t\t' + format(km, '8.3f') + ' km')
print('Gas\t\t\t: ' + format(gallons, '8.3f') + ' gallons\t\t' + format(liters, '8.3f') + ' liters')
print('Consumption\t: ' + format(mpg, '8.3f') + ' mpg\t\t\t' + format(cm, '8.3f') + ' 1/100km')
print('Gas consumption rating: ' + rating)

