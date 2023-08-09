# Nested if statement

height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are slightly overweight')
elif bmi > 18.5 & weight < 25:
    print(f'Your BMI is {bmi}, you are normal')
