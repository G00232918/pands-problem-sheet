# Calculating a person's BMI
# Author: James Connolly

# Person's details listed below as per assignment requirement
# Enter weight (kg): 65
# Enter height (cm): 180
# The BMI is (kg/m2) 20.06

# Print person's name
name = input("enter your name:")
print("Hello " + name)

# enter your weight
# Use float numbers to give user option to put in more
# accurate weights
weight = float(input("input your weight in Kilogram: "))

# enter your height
# Use float numbers to give user option to put in more
# accurate height details
height = float(input("Input your height in cm: "))

# BMI calculation 
# BMI answer rounded to decimal places with the round fucntion before calculation
# Round command used to round up the answer to 2 decimal places in this example
print ("Your BMI is =", round(weight / (height/100)**2, 2))


