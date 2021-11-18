import numpy as np
print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

true_love_calculator = "true love"
list_name1 = []
for char in name1:
    name1_char = char.lower()
    list_name1.append(name1_char)

list_name2 = []
for char in name2:
    name2_char = char.lower()
    list_name2.append(name2_char)

list_true_love = []
for char in true_love_calculator:
    true_love_calculator_char=char.lower()
    list_true_love.append(true_love_calculator_char)

total_name = name1+name2
# print(total_name)

t = total_name.count("t")
r = total_name.count("r")
u = total_name.count("u")
e = total_name.count("e")
true = t+r+u+e

l = total_name.count("l")
o = total_name.count("o")
v = total_name.count("v")
e = total_name.count("e")
love = l+o+v+e

true_love = int(str(true)+str(love))
if (true_love<10) or (true_love>90):
    print(f"Your love score is {true_love}, You two are like coke and mentos")
elif (true_love>=40) and (true_love<=50):
    print(f"Your love score is {true_love}, You are alright together")
else:
    print(f"Your love score is {true_love}")


