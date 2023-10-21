import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if match := re.search(r"(\d{1,2}):?(\d{1,2})? (AM|PM) to (\d{1,2}):?(\d{1,2})? (AM|PM)", s):
        #search input and sort into groups
        start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()
        start_hour = int(start_hour)
        start_minute = int(start_minute) if start_minute else 0
        end_hour = int(end_hour)
        end_minute = int(end_minute) if end_minute else 0
        #Convert all PM times to 24 hour format
        if start_period == "PM" and start_hour != 12:
            start_hour += 12
        if end_period == "PM" and end_hour != 12:
            end_hour += 12
        #Convert all AM times to 24 hours format
        if start_period == "AM" and start_hour == 12:
            start_hour -= 12
        if end_period == "AM" and end_hour == 12:
            end_hour -= 12
       #Check if minutes are greater than 59
        if start_minute > 59 or end_minute >59:
            raise ValueError
        converted_time = f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
        return converted_time
    else:
        raise ValueError

if __name__ == "__main__":
    main()