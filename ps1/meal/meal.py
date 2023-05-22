def main():
    # Gets input and converts it to hours in float
    time = convert(input("What time is it? "))

    # Output
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# Splits the time into hours and minutes and calculates time in hours
def convert(time):
    hour, minute = time.split(":")
    return float(hour) + (float(minute) / 60)

if __name__ == "__main__":
    main()