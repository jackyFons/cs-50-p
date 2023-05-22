def main():
    perc = convert(input("Fraction: "))
    print(gauge(perc))


def convert(fraction):
    try:
        frac = fraction.split("/")
        num, denom = [int(f) for f in frac]
        if denom == 0:
            raise ZeroDivisionError
        if num > denom:
            raise ValueError()
        percent = round(int(num) / int(denom) * 100)
        return percent
    except ValueError:
        raise ValueError
    

# Calculates percentage, returns percentage, E, or F
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()