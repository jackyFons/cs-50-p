import inflect

i = inflect.engine()
# Holds names in a list
names = []

def main():
    while True:
        # Adds name to list
        try:
            names.append(input("Name: "))
        # Stops program with control-d and prints line
        except EOFError:
            print( "Adieu, adieu, to " + i.join(names))
            break

main()