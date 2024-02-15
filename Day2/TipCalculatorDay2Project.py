print("Welcome to tip calculator")
total_bill= input("What was the total bill?")
tip_percent=input("What percentage tip would you like to give ? ")
total_people=input("How many people to spolit the bill? ")
percentage =int(tip_percent)/100*float(total_bill)
total_money=float(total_bill)+float(percentage)
payed=float(total_money)/int(total_people)

print (f'Each person should pay {round(payed,2)}')