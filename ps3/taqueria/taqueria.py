menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    # Gets items
    while True:
        try:
            item = input("Item: ").title()
            # If item exists in the menu, add its price to the total
            if item in menu:
                total += menu[item]
                # Formats total as $##.##
                print("Total: ${:.2f}".format(total))
        # Ends program with control-d
        except EOFError:
            break

main()