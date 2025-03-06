print("\nWelcome to Python Pizza Deliveries.\n")

print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")
size = input("What pizza size would you like(S/M/L): ").upper()

print("\n")
print("Pepperoni for Small Pizza: +$2")
print("Pepperoni for Medium or Large Pizza: +$3")
add_pepperoni = input("Which pepperoni option would you like(Y/N): ").upper()


print("\n")
print("Cheese: +$1")
extra_cheese = input("Would you like extra cheese on your pizza(Y/N)? ").upper()

#initialize the bill
bill= 0

if size =="S":
    bill+= 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

#Add pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


# Add cheese
if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: {bill}")