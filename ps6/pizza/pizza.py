import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    table = []
    with open(sys.argv[1]) as o_file:
        reader = csv.reader(o_file)
        header = next(reader)
        for line in reader:
            table.append(line)
    print(tabulate(table, header, tablefmt = "grid"))
except FileNotFoundError:
    sys.exit("File does not exist")