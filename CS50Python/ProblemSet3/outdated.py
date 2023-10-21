#Month's List
months = [
    "January","February","March","April","May","June",
    "July","August","September","October","November",
    "December"
]

while True:
    user_date = input("Date: ")
    try:
        o_month, o_day, year = user_date.split()
        for i in range(len(months)):
            if o_month == months[i]:
                month = i + 1
        if "," in user_date:
            day = o_day.rstrip(",")
        if 1 <= int(month) <=12 and 1 <= int(day) <=31:
            break
    except:
        try:
            month, day, year = user_date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            pass
year = int(year)
month = int(month)
day = int(day)

f_date = f"{year}-{month:02d}-{day:02d}"
print(f_date)



