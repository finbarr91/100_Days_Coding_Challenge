# Functions with output
first_name = input("Type your first name")
last_name = input("Type your last name")

def format_name(f_name, l_name):
    """Takes a first and last name and format it to return
    the title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_str =format_name(f_name=first_name,l_name=last_name)
print(formatted_str)



def is_leap(year):
    """Takes the year as an argument and check if it is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month>12 or month<1:
        return "Invalid month"
    if is_leap(year) and month ==2:
        return 29
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



# Add
def add(n1,n2):
    """Takes two numbers and computes the sum"""
    return n1+n2

# Subtract
def subtract(n1,n2):
    """Takes two numbers and subtracts one number from the other"""
    return n1-n2

# Multiply
def divide(n1,n2):
    """Takes two numbers computes the division"""
    return n1/n2

# Divide
def multiply(n1,n2):
    """Takes two numbers and computes the multiplication"""
    return n1*n2

operations = {
        "+" : add,
        "-" : subtract,
        "/" : divide,
        "*" : multiply
        }
def calculator():
    num1 = float(input("What is the first number?: "))


    for symbol in operations:
        print(symbol)


    end = False
    while not end:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))
        calculation_function= operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        continue_operation = input(f"Do you want to use {answer} to continue operation, Type'y' or 'n' ").lower()
        if continue_operation == 'y':
           num1 =answer
        else:
            end = True
            calculator()

calculator()



