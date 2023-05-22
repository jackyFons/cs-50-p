def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print(f"${val}")


def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting.startswith("hello"):
        return  0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()