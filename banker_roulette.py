import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
items=len(names)
print(items)
random_pick= random.randint(0,items-1)
pick=names[random_pick]
print(pick + "is going to buy the meal today!")
