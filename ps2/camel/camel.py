# Gets camelCase input
camel = input("camelCase: ")

# empty string for snake_case
snake = ""

#iterates camel case, detecting uppercase characters
for c in camel:
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c

print(snake)