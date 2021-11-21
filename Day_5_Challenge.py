# # Calculating the average of student heights without using the sum and len functions challenge
# 
# student_heights = input("Input a list of student heights").split()
# 
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# 
# total_height =0
# for height in student_heights:
#     total_height = total_height + height
# print(total_height)
# 
# number_of_students = 0
# for student in student_heights:
#     number_of_students = number_of_students+1
# print(number_of_students)
# 
# 
# average = total_height/number_of_students
# print(average)
# 


# Calculating the highest score from a list of scores.
# student_scores = input("Input a list of student scores").split()
# for n in range(0,len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for score in student_scores:
#     if score> highest_score:
#         highest_score = score
# print(highest_score)
#
# lowest_score = 1
# for score in student_scores:
#     if score<lowest_score:
#         lowest_score=score
# print(lowest_score)

#
# # Using a for loop to sum number from 1 to 100
#
# total = 0
# for number in range(0,101):
#     total = total + number
# print(total)

# Write a code that sums even numberr between 1 to 100 inclusive

# total_even_numbers = 0
# for even_numbers in range(0,101,2):
#     total_even_numbers = total_even_numbers+even_numbers
# print(total_even_numbers)

# total = 0
# for even_number in range(1,101):
#     if even_number%2 ==0:
#         total = total +even_number
# print(total)

# The Fizzbuzz challenge
#
# for divisible_numbers in range(1,101):
#     if divisible_numbers % 3 == 0 and divisible_numbers % 5 == 0:
#         print("FizzBuzz")
#     elif divisible_numbers%3 ==0:
#         print("Fizz")
#     elif divisible_numbers %5 ==0:
#         print("Buzz")
#     else:
#         print(divisible_numbers)

# Password Generator Project

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would your like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_gen = []
for letter in range(nr_letters):
    password_letter = random.choice(letters)
    password_gen.append(password_letter)
for number in range(nr_numbers):
    password_number = random.choice(numbers)
    password_gen.append(password_number)
for symbol in range(nr_symbols):
    password_symbol = random.choice(symbols)
    password_gen.append(password_symbol)
password_generator = password_gen
print(password_generator)
shuffled_password = random.sample(password_generator, len(password_gen))
print(shuffled_password)

password = ""
for char in shuffled_password:
    password= password+char
print(password)





