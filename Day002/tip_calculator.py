print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_percentage = tip/100 * bill
total_bill = bill + tip_percentage
bill_per_person = round(total_bill / people, 2)
print("Each person should pay: $" + str(bill_per_person))