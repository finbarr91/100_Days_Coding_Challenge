# Challenge
# Calculating the number of months, days and weeks remaining in your life if you were to live for 90 years.

age = input("What is your Age?")
age_as_int = int(age)
days_in_a_year = 365
months_in_a_year = 12
weeks_in_a_year =52

maximum_age = 90
number_of_months_in_90 = maximum_age*months_in_a_year
number_of_weeks_in_90 = maximum_age* weeks_in_a_year
number_of_days_in_90 = maximum_age*days_in_a_year

number_of_months_in_current_age = age_as_int*months_in_a_year
number_of_weeks_in_current_age = age_as_int*weeks_in_a_year
number_of_days_in_current_age = age_as_int*days_in_a_year

number_of_months_left = round(number_of_months_in_90-number_of_months_in_current_age)
number_of_weeks_left = round(number_of_weeks_in_90-number_of_weeks_in_current_age)
number_of_days_left = round(number_of_days_in_90-number_of_days_in_current_age)

message = f"You have {number_of_days_left} days, {number_of_weeks_left} weeks, and {number_of_months_left} months left."
print(message)

# Another solution
age = input("What is your Age?")
age_as_int = int(age)
maximum_age = 90

years_remaining = maximum_age-age_as_int

number_of_days_remaining = years_remaining*365
number_of_months_remaining = years_remaining*12
number_of_weeks_remaining = years_remaining*52

message = f"You have {number_of_days_remaining} days, {number_of_weeks_remaining} weeks, and {number_of_months_remaining} months left."
print(message)