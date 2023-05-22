import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^.*src=\"https?://(www\.)?youtube\.com/embed/([0-9a-zA-z]+)\"", s):
       return "https://youtu.be/" + match.group(2)
    else:
        return None

if __name__ == "__main__":
    main()