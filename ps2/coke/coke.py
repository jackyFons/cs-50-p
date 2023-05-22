# Amount user needs for a coke
due = 50

# Coins that are accepted by the machine
accepted = [5, 10, 25]

# Keep prompting user until they deposit 50 cents
while due > 0:
    deposit = int(input("Insert Coin: "))
    # Accepts only if coin is a 5, 10, or 15
    if deposit in accepted:
        due -= deposit
    # Prints amount owed only if the amount due is over 0
    if due > 0:
        print("Amount Due: " + str(due))

# Prints amount owed
print("Change Owed: " + str(abs(due)))