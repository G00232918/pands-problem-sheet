# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: James Connolly

# request for user to input a positive float number
number = float(input("Please enter a positive number: "))

# function to reject negative numbers using an if statement
def positveNum(number):
    if number >= 0:
        return True
    else:
        return False

# function based on Newtons square root method
def sqRt(value): 
 # take te float value, can be taken as the guess   
    a = float(value)

# number of iterations is based on Newtons square root method where 
# the function needs to run many times to get the correct approx answer
    number_iters = 100
    for i in range(number_iters):
        value = 0.5 * (value + a / value)
    return round(value, 1)

# when the number is postive the answer is to be printed with the number
# requested at the beginning and the answer of the sqRT function
if positveNum(number) == True:
    print("The square root of {} is approx. {}".format(number, sqRt(number)))
else:
    print ("Please enter a positive number!")
