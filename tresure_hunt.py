#task tresure hunt
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input(" Entered the Island!!! Where would you like to move? left or right? ").lower()
if direction == "right":
    print("wrong step!!! Game Over")
else:
    door = input("which door would you like to open? red,blue,green ").lower()
    if door =="red":
        print("Fire!!!! Game over")
    elif door =="blue":
        print("fell into water!!!")
    else:
        prize = input("Final round!!!! /n Which box would you lie to open? 1 or 2 or 3? ")
        if prize =="1":
            print("Won!! gold items")
        elif prize =="2":
            print("dead!!! box with snakes")
        else:
            print("oops!!! no luck!! Empty box")
#created random game with help of conditions.            
