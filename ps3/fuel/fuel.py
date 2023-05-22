
def main():
    output(to_percent())


# Calculates percenrage, returns percentage, E, or F
def output(p):
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")

# Prompts user for a fraction until a valid one is given
def to_percent():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            num, denom = [int(f) for f in fraction]
            if num > denom:
                continue
            percent = round(int(num) / int(denom) * 100)
            return percent
        except (ValueError, ZeroDivisionError):
            pass

main()