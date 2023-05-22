import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a python file")

try:
    line_count = 0
    with open(sys.argv[1], "r") as o_file:
        for line in o_file:
            if line.isspace() == False and line.lstrip().startswith("# ") == False:
                line_count += 1
    print(line_count)
except FileNotFoundError:
    sys.exit("File does not exist")
