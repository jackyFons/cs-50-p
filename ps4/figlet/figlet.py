import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
# Two arguments
if len(sys.argv) == 3:
    # Makes sure the first argument is -f or --font
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        f = sys.argv[2]
        # Changes font if it exists
        if f in figlet.getFonts():
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit(-1)
    else:
        sys.exit(-1)
# No argument
elif len(sys.argv) == 1:
    # Sets font to a random one
    random_font = choice(figlet.getFonts())
    figlet.setFont(font = random_font)
# 1 or more than 2 arguments
else:
    sys.exit(-1)

inp = input("Input: ")
print(figlet.renderText(inp))