# dictionary to store list of groceries
g_list = {}

def main():
    while True:
        try:
            item = input().upper()
            # Adds + 1 to the amount
            if item in g_list:
                g_list[item] += 1
            # Adds item to list and sets amount to 1
            else:
                g_list[item] = 1
        # Ends user input with control-d, lists every item in alphabetical
        # order, with amount in front
        except EOFError:
            for k, v in sorted(g_list.items()):
                print(f"{v} {k}")
            break

main()