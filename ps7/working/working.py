import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^([0-1]?[0-9]):?([0-5][0-9])? (AM|PM) to ([0-1]?[0-9]):?([0-5][0-9])? (AM|PM)", s):
        if int(match.group(1)) > 12 or int(match.group(4)) > 12:
            raise ValueError
        return get_time(int(match.group(1)),  match.group(2),  match.group(3)) + " to " \
        + get_time(int(match.group(4)),  match.group(5),  match.group(6))
    else:
        raise ValueError


def get_time(hour, min, type):
    if type == "AM" and hour == 12:
        hour = 0
    elif type == "PM" and hour == 12:
        pass
    elif type == "PM":
        hour += 12
    return f"{hour:02}:{get_min(min):02}"


def get_min(n):
    if n == None:
        return 0
    else:
        return n


if __name__ == "__main__":
    main()