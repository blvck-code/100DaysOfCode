print('Welcome to the tip calculator.')
bill = float(input('What was the total bill ? '))
tip = int(input('What percentage tip would you like ti give? 10, 12, or 15 ? '))
people = int(input('How any people to split the bill ? '))

total_bill = bill + (tip / 100 * bill)
# pay = round(total_bill / people, 2)
pay = total_bill / people
message = "{:.2f}".format(pay)
# print(f'Each person should pay: ${pay}')
print(f'Each person should pay: ${message}')
