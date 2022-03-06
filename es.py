# a program that reads in a text file and outputs 
# the number of e's it contains

import sys

# renaming the file to be ran through the command line
filename = sys.argv[1]

# opens the text file as read text
with open(sys.argv[1], "rt") as text_file:
# this reading the text file    
    lyrics = text_file.read()
# from the text file, this is to count the lower case es as requested.
# Usual practice in IT is to confirm the exact requirements.
# So in this case I am only calling the lower es.
    number_of_es = lyrics.count("e")

# print statement to confirm the amount of es in the text file
print ("The number of es is {}".format(number_of_es))


