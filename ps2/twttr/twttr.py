# Vowels to be removed
vowels = ["a", "e", "i", "o", "u"]

# Gets input and removes all vowels
inp = input("Input: ")
outp = ""
for c in inp:
    if c.lower() not in vowels:
        outp += c

# Prints string without vowels
print(outp)