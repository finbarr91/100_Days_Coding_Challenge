import math
import pandas

# # Simple function
# def greet():
#     print("I am here with you")
#     print("I am here with you")
#     print("I am here with you")
# greet()

# Function with input

# def greet(name):
#     print(f"My name is {name}")
#     print(f"How are you {name}")
#
# greet("Finbarr")
#
# Function with more than one input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in your {location}")
#
# greet_with("Finbarr", "Phoenix Arizona")
#
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in your {location}")
#
# greet_with(location='Phoenix Arizona', name="Finbarr")

# #Calculating the number of paints used for painting
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# def paint_cal(width,height,cover):
#     area = height*width
#     number_of_cans = math.ceil(area/cover)
#     print(f"You will need {round(number_of_cans)} cans of paint.")
#
# paint_cal(height=test_h, width=test_w,cover=coverage)

# Prime number checker
def prime_checker(number):
    is_prime =True
    for i in range(2,number):
        if number%i ==0:
            is_prime =False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")



n = int(input("Check this number:"))
prime_checker(number=n)
