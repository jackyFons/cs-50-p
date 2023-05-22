from datetime import date
import sys
import inflect

i = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    return print(validate(dob) + " minutes")


def validate(dob):
    try:
        year, month, day = dob.split("-")
        birth = date(int(year), int(month), int(day))
        minutes = (date.today() - birth).days * 24 * 60
        return num_to_words(minutes)
    except:
        sys.exit("Invalid")

def num_to_words(n):
    return i.number_to_words(n, andword="").capitalize()


if __name__ == "__main__":
    main()