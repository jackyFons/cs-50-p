import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    people = []
    with open(sys.argv[1]) as r_file:
        reader = csv.DictReader(r_file)
        for line in reader:
            last, first = line["name"].split(", ")
            people.append({"first": first, "last": last, "house": line["house"]})

    with open(sys.argv[2], "w") as w_file:
        writer = csv.DictWriter(w_file, people[0].keys())
        writer.writeheader()
        writer.writerows(people)

except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])
