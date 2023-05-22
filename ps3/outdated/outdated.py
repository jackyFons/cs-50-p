months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    formatted = get_date()
    print(formatted)

def get_date():
    # Gets middle-endian date from user
    while True:
        try:
            mid_en = input("Date: ").strip()
            # MM/DD/YYYY format
            if "/" in mid_en:
                month, day, year = mid_en.split("/")
                # Get another date, as this one is not valid
                if int(day) > 31 or int(month) > 12:
                    continue
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            # {Month} {DD}, {YYYY} format
            elif "," in mid_en:
                month_day, year = mid_en.split(", ")
                month, day = month_day.split(" ")
                # Get another date, as this one is not valid
                if int(day) > 31 or month not in months:
                    continue
                return f"{year}-{months.index(month)+1:02}-{day.zfill(2)}"
        except ValueError:
            continue


main()