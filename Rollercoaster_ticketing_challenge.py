height = float(input("What is your height in cm"))
bill = 0
if height >=120:
    print("print you can ride")
    age = int(input("Enter your age"))
    if age<12:
        bill = 5
        # print("Child ticket is 5$")
    elif age<=18:
        bill = 7
        # print("Your ticket is 7$")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay, Your ride is on us")
    else:
        bill = 12
        # print("Your ticket is $12")

    want_photo = input("Do you want your photo to be take, Y or N")
    if want_photo == 'Y':
        bill +=3
    print(f'Your total bill is {bill}')


else:
    print("Can't ride")