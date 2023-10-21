#Prompt User for the Time
#Output Whether it's Breakfast, Lunch, or Dinenr Time.
#If its not any of the above times, output nothing at all
def main():
    given_time = input("What time is it? ")
    converted_time = convert(given_time)
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time >=18 and converted_time <= 19:
        print("dinner time")



#Convert time to be used in a conditional statement in main function
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()




