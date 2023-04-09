print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height>=120:
  print("You can have a ride!!!!!")
  age = int(input("What is your age: "))
  if age < 12:
    bill = 5
    print("Children pay $5.")
  elif age <= 18:
    bill = 7
    print("Youth pay $7.")
  else: 
    bill = 12
    print("Adult pay $12.")
  photo = input("Do you want photo: Y or N.")
  if photo =="Y":
    bill += 3
  print(f"Your final bill is {bill}")
    
else:
  print("sorry!grow more!!!")
