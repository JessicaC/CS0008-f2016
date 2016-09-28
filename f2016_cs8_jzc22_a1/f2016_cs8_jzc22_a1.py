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
distance = float(input("Distance driven: "))
gasoline = float(input("Gasoline used: "))
# Print the amounts
if sys == 'USC':
    print(format(distance, ',.3f'), \
          ' miles', sep='')
    print(format(gasoline, ',.3f'), \
          ' gallons', sep='')
elif sys == 'Metric':
    print(format(distance, ',.3f'), \
          ' km', sep='')
    print(format(gasoline, ',.3f'), \
          ' liters', sep='')
# Convert the quantities
if sys == 'USC':
    newdis = distance * 1.60934
    newgas = gasoline * 3.78541
    print(format(newdis, ',.3f'), \
          ' km', sep='')
    print(format(newgas, ',.3f'), \
          ' liters', sep='')
elif sys == 'Metric':
    newdis = distance / 0.621371
    newgas = gasoline / 0.264172
    print(format(newdis, ',.3f'), \
      ' miles', sep='')
    print(format(newgas, ',.3f'), \
      ' gallons', sep='')
# Compute the fuel consumption
c_mpg = distance / gasoline
cm = (distance * 100) / gasoline
print(format(c_mpg, ',.3f'), \
     ' mpg', sep='')
print(format(cm, ',.3f'), \
     ' 1/100km', sep='')
# Consumption rating
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

print('\t\t\t\tUSC\t\tMetric')


print('Gas consumption rating: ' + rating, sep='')
