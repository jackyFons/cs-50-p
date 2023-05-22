import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if match := re.findall(r"\b[U-u]m\b", s):
        return len(match)


if __name__ == "__main__":
    main()