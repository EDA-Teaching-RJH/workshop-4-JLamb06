drink3 = False
while drink3 == False:
    drink1 = input("Would you like a hot chocolate, a coffee or a tea? ")
    drink2 = drink1.lower().strip()
    if drink2 == "hotchocolate":
        amount = 125
        drink3 = True
    elif drink2 == "coffee":
        amount = 110
        drink3 = True
    elif drink2 == "tea":
        amount = 100
        drink3 = True
    else:
        print("Sorry but we don't have that type of drink. Please enter a drink from the drinks above. ")

shot3 = False
while shot3 == False:
    shot1 =input("Would you like an extra shot? ")
    shot2 = shot1.lower().strip()
    if shot2 == "yes":
        amount = amount + 25
        shot3 = True
    elif shot2 == "no":
        amount = amount + 25
        shot3 = True
    else:
        print("Please enter yes or no")

money1 = 0

print("This machine only accepts 50p, 20p, 10p and 5p")
print("Your drink costs ", amount)

while money1 < amount:
    money2 = int(input("Input your money: "))
    if money2 == 50 or money2 == 20 or money2 == 10 or money2 == 5:
        money1 = money1 + money2
        if money1 < amount:
            print ("You have inserted", money1, "You need to insert", amount - money1, "more")
        elif money1 > amount:
            change = money1 - amount
            print("Please take your change of", change)
        else:
            print ("You have inserted the exact amount, have a nice day.")
    else:
        print("Sorry, this machine doesn't accept that currency. This machine only accepts 50p, 20p, 10p and 5p, you still")