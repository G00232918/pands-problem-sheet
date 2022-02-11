# A program that asks the user to input any positive integer and outputs the successive
# values of the calculation. 
# At each step calculate the next value by taking the current value and, if it is even,
# divide by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# requests the user to input a postive integer

def collatz(number):
    # modulus command to confirm is the number even
    if number % 2 == 0:
        # return to show the value rounded divided by 2           
        return round (number / 2)
    # elseif with modulus to confirm if the number is odd
    elif number % 2 == 1:
      # return to show the value multiplied by 3 plus 1          
      return (3 * number + 1)

# request for user to input a positive integer
print ("please enter a postive integer: ")
number = int(input())  

# while until it reaches one
while number != 1: 
    print (number)
    # confirm the number is equal to the function
    number = collatz(number)
# print the values of the while loop    
print (number)
# reaches 1, the message is goodbe    
print ("goodbye")
    