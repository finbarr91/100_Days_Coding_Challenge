print("Welcome to the tip Calculator!")

total_bill = float(input('What is the total bill? $'))
percentage_tip = int(input("What percentage tip would you like to give? 10,12 or 15"))
number_of_people_splitting_the_bill = int(input('How many people to split the bill?'))

# Calculating the percentage tip with respect 10,12,15 percentage
total_bill_with_tip = percentage_tip/100*total_bill + total_bill
amount_each_person_has_to_pay = total_bill_with_tip/number_of_people_splitting_the_bill

final_amount = round(amount_each_person_has_to_pay,2)
final_amount = "{:.2f}".format(amount_each_person_has_to_pay)

print(f"Each person should pay: ${final_amount}")
