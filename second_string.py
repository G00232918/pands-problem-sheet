# A program that requests a user to input a string and outputs every second 
# letter in reverse order.
# Author: James Connolly

# variable defined with the request for the user to input the string to be reversed 
sentence = input("Input a sentance which you require to reverse: ")


# the slice statement which means start at the end of the string and end at position 0, 
# move with the step -2, negative two, which means two step backwards.
print (sentence[::-2])

