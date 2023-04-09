print("Welcome to tip calculator.")
bill= float(input("What is you total bill $ "))
tip = int(input("What amount of the tip would you like to give? 10, 12, or 15? "))
split = int(input("how many ppl to split the bill?" ))
# percentage = number/100
# percentage of number = percentage* number
#percentage total = percentage of number +total
bill_with_tip = tip/100 *bill +bill
bill_per_person = round(bill_with_tip/ split , 2)
#bill_per_person = "{:.2f}".format(bill_with_tip)
print(f"Final amount to pay is ${bill_with_tip}, and each person should pay ${bill_per_person}")
