#Calculating the BMI of people
height = input('Enter your height in m:')
weight = input('Enter your weight in Kg:')

# BMI
BMI = float(weight)/float(height)**2
BMI_as_int = int(BMI)
print(BMI_as_int)
