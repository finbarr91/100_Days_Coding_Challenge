# Data Types

# String

print('Chukwuka'[0:4])

"1233478" # is a string

# Integer- All whole numbers whether positive or negative are called Intergers
print(123 + 456)
print(123_456_789)

# Float
pi = 3.14159

# Boolean
True
False

print(len('Chukwuka'))

num_char = len(input('What is your name?'))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has"+ " "+new_num_char+" "+ "characters")
print(type(num_char))

a = str(100)
print(type(a))
print(70 + float("100.5"))

# Day 2 Coding Challenge:

two_digits_number =input("Type a two digit number:")
print(type(two_digits_number))
first_digit= int(two_digits_number[0])
second_digit= int(two_digits_number[1])
result= first_digit + second_digit
print(result)
#
# Mathematical Operation
3 +5
7-4
6/2 # the result is a float
2**3 # 2 raise to the power of 3. or 2 exponential 3
# It uses PEMDAS for mathematical operation
#
# Calculating the BMI of people
height = input('Enter your height in m:')
weight = input('Enter your weight in Kg:')

# BMI
BMI = float(weight)/float(height)**2
BMI_as_int = int(BMI)
print(BMI_as_int)
#
# Rounding to a two decimal places
print(round(2.66666678787,2))
print(8//3)

result = 4/2
result /=2

score = 0
score +=1
print('your score is' + str(score))

score = 0
height = 1.8
isWinning = True

# f-String
print(f"your score is {score}, your height is {height},you are winning is {isWinning}")



print(6+4/2-(1*2))

a= int("5")/int(2.7)
print(type(a))
