# Gets input "x y z", places each into a variable
x, y, z = input("Expression: ").split(" ")

# Calculates the expression as a float
if y == "+":
    print(float(int(x) + int(z)))
elif y == "-":
    print(float(int(x) - int(z)))
elif y == "*":
    print(float(int(x) * int(z)))
else:
    print(float(int(x) / int(z)))