def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Returns false if plate does not have 2 - 6 characters
    if len(s) < 2 or len(s) > 6:
        return False
    # Returns false if plate is not alphanumeric
    elif s.isalnum() == False:
        return False
    # Return true if plate is all letters
    elif s.isalpha() == True:
        return True

    # In case of plate being alphanumeric
    for i, c in enumerate(s):
        if c.isnumeric():
            # Returns false if the first number is 0
            if c == "0":
                return False
            end = s[i:]
            # Returns false if the plate contains letters after numbers
            if end.isnumeric() == False:
                return False
            # Returns true if there are no letters after numbers
            else:
                return True

main()