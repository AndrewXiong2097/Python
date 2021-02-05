'''
The Objective is to make a program that can complete different conversions.The tasks to complete are:
Have the user input a number of miles. Convert the number of miles to yards, feet, and inches.
Print out the conversions with a simple statement:
EX: 
    "[mileInt] converts to [feetInt] feet."
    "[mileInt] converts to [yardInt] yards."


@author: Andrew
'''


#Use input(10) to get the number of miles from the user. And store
#that int in a variable called miles.
miles = 10
#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.
yards = miles * 1760
print(str(miles) + " converts to " + str(yards) + " yards.")
#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.
feet = miles * 5280
print(str(miles) + " converts to " + str(feet) + " feet.")
#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.
inches = miles * 63360
print(str(miles) + " converts to " + str(inches) + " inches.")