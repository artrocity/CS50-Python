from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthday = check_dob(input("Date of Birth: "))
    current_date = get_current_date()
    age = calc_age(birthday, current_date)
    minutes_age = convert_age(age).capitalize()
    print(f"{minutes_age} minutes")


def check_dob(dob):
    #formtatted as follows: YYYY-MM-DD 00:00
    if match := re.search(r"\d{4}-\d{2}-\d{2}", dob):
        dob_str = match.group()
        dob = date.fromisoformat(dob_str)
        return dob
    else:
        sys.exit("Invalid Date")

#get current date
def get_current_date():
    result = date.today()
    return result

#calculate current age
def calc_age(dob, current_date):
    age = current_date - dob
    return age

#convert age to minutes
def convert_age(age):
    age_in_days = age.days
    #Round to the nearest integer
    age_minutes = age_in_days * 24 * 60
    rounded_age_minutes = round(age_minutes)
    #Print how old they are in english words without using and - inflect
    inflect_age = p.number_to_words(rounded_age_minutes, andword="", zero="zero")
    return inflect_age

if __name__ == "__main__":
    main()


