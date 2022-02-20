# Write a program that outputs whether or not today is a weekday.
# Author: James Connolly

# importing the datetime module
import datetime

# setting up the variable to pull the integer for today and the weekday
dayToday = datetime.datetime.now().weekday()

#if the integer is less that 5 it will return in the index it will return the print
if dayToday <5:
    print ("Yes, unfortunately today is a weekday.")

# if the number in index is 5 or more it will return the print message
else:
    print ("It is the weekend, yay!")



