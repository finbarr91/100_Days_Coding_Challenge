print("Welcome to Python Pizza")
size  = input("What size of pizza do you want? L,S,M")
add_pepperoni = input("Do you want to add Pepperoni?")
add_extra_cheese = input("Do you want to add extra cheese?")

bill =0
if size == "L" :
    bill+=25
elif size == "M" :
    bill+=20
else:
    bill +=15

if add_pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
if add_extra_cheese == "Y" :
    bill+=1

print(f"your final bill is : ${bill}")



