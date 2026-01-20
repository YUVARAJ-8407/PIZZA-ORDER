bill=0

print("Welcome to Python Pizza Deliveries")
size=input("What sized pizza do you want: 'S','M' or 'L'").upper()
pepperoni=input("Do you want pepperoni on your pizza: 'Y' or 'N'").upper()
extra_cheese=input("Do you want extra cheese: 'Y' or 'N'").upper()
prices1={"S":20,"M":25,"L":30}
prices2={"S":2,"M":3,"L":3}

if size in prices1:
    bill+=prices1[size]
else:
    print("You typed an invalid pizza size")
    exit()

if pepperoni=="Y":
    bill+=prices2[size]
elif pepperoni!="N":
    print("You typed an invalid pepperoni choice")

if extra_cheese=="Y":
    bill+=1
elif extra_cheese!="N":
    print("You typed an invalid extra cheese choice")

print(f"The final bill: ${bill}")
print("Thank you for placing the order")