import random
import numpy as np
# Printing Head or tail from a coin toss
heads_tail = random.randint(0,1)
print(heads_tail)
if heads_tail == 0:
    print("Tails")
else:
    print("Heads")

# Challenge of who is going to pay for the meals after putting the business cards in the bowl
names_string = input(" Give me everybody's names, separated by a coma.")
names = names_string.split(",")
print(names)
random_names = random.randint(0,len(names)-1) #len(names)-1 because randint doesnt not include the upper bound rather upper bound-1
print(random_names)
selected_name = names[random_names]
print(f"{selected_name} will pay the bill of today")

# Another way of doing this is by using the random choice function
random_names = random.choice(names)
print(f"{random_names} will pay the bill of today")


list = ['Chisom', 'Chuka', 'Kilinki']
print(len(list))
print(list[2])


fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","Kale","Celery","Potatoes"]

dirty_dozens = [fruits,vegetables]

print(dirty_dozens[0][1])
print(dirty_dozens[1][1])

# Playing Chase

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3=  [" ", " ", " "]

map= [row1,row2,row3]

print(map)


position = input("Where do you want to put the treasure 'X'")
row = int(position[0])
column = int(position[1])

result= map[row-1][column-1]="X"
print(f"{row1}\n {row2}\n {row3}")

 # Rock Paper Scissors ASCII Art

Rock = """ Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """ Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """ Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

if choice == 0 or choice == Rock:
    print(f"You chose {Rock}")
elif choice == 1 or choice == paper:
    print(f"You chose {paper}")
elif choice == 2 or choice == Scissors:
    print(f"you chose {Scissors}")

choice_machine= [Rock, paper, Scissors]


computer_choice = random.choice(choice_machine)
print(f"The computer choice is {computer_choice}")

if choice == Rock or choice == 0 and computer_choice == Scissors:
    print("You win")
elif choice == Scissors or choice == 2 and computer_choice == paper:
    print("You win")
elif choice == paper or choice == 1and computer_choice == Rock:
    print("You win")
elif choice == Scissors or choice ==2 and computer_choice == Rock:
    print("You lose")
elif choice == paper or choice == 1 and computer_choice == Scissors:
    print("You lose")
elif choice == Rock or choice == 0  and computer_choice == paper:
    print("You lose")
elif choice == Rock or choice == 0 and computer_choice== Rock:
    print("Draw")
elif choice == Scissors or choice ==2 and computer_choice == Scissors:
    print("You draw")
elif choice == paper or choice == 1 and computer_choice == paper:
    print("You draw")
else:
    print("You entered an invalid number therefore you lose")


