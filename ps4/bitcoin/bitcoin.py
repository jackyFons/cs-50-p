import sys
import requests

# 0 or more than 1 argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    # Converts user input into float
    n = float(sys.argv[1])

    # Generates bitcoin rate
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    out = response.json()
    rate = out["bpi"]["USD"]["rate_float"]
    amount = n * rate
    print(f"${amount:,.4f}")

# Argument is a not a float
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit(-1)