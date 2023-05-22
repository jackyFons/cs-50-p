import random
import sys


def main():
    level = get_level()
    # Keeps track of how many answers were correct
    score = 0

    # Creates 10 equations
    for i in range(10):
        # Creates equation with random integers
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y

        # Gives user 3 chances to get the correct answer
        for j in range(3):
            # Gets users answer
            user_ans = input(f"{x} + {y} = ")

            # Checks if user's answer was correct
            if str(ans) == user_ans:
                score += 1
                break
            # Prints "EEE" if answer is incorrect and prints the correct answer
            # if the user used up all attempts
            else:
                print("EEE")
                if (j == 2):
                    print(ans)
    # Gives user their score
    print(f"Score: {score}")
    sys.exit()


# Retrieves level from user input
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            # Checks that the level is 1, 2, or 3
            if level < 1 or level > 3:
                continue
            else:
                return level
        # Input was not an integer
        except ValueError:
            pass

# Creates random numbers depending on level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()