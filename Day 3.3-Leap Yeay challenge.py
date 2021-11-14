# # Leap Year Challenge

year = int(input(" Which year do you want to check?"))

if year % 4 ==0 and (year % 100 != 0 or year % 400==0 ):
    print(f"{year}is a Leap year")
else:
    print("Not a leap year")

if year % 4 == 0 :
    if year % 100 ==0:
        if year % 400 ==0:
            print("This is leap")
        else:
            print("This is not a leap")
    else:
        print(" This is a leap year")
else:
    print("Not a leap year")

