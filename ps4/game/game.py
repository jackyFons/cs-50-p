import sys
from random import randrange

def main():
    level = get_level()
    answer = randrange(1, level+1) # Creates a random number between 1 and the level
    get_guess(answer)

# Prompts user until they give a positive integer
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            return level
        except ValueError:
            pass

# Prompts user until they guess the correct number
def get_guess(answer):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            pass

main()