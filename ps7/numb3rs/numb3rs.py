import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
        for num in match.groups():
            if int(num) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()