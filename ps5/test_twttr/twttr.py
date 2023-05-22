def main():
    short = shorten(input("Input: "))
    print(short)


# Gets input and removes all vowels
def shorten(word):
    # Vowels to be removed
    vowels = ["a", "e", "i", "o", "u"]
    outp = ""
    for c in word:
        if word.lower() not in vowels:
            outp += c
    return outp


if __name__ == "__main__":
    main()