import re
import sys

#main fucntion asking for input
def main():
    print(validate(input("IPv4 Address: ")))

#Verifies input is valid IPv4 address
def validate(ip):
    #set search parameters
    match  = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)

    #convert match groups to int
    if match:
        oct1 = int(match.group(1))
        oct2 = int(match.group(2))
        oct3 = int(match.group(3))
        oct4 = int(match.group(4))

        #check if groups are between 0-255
        if (0 <= int(oct1) <= 255) and (0 <= int(oct2) <= 255) and (0 <= int(oct3) <= 255) and (0 <= int(oct4) <= 255):
            return True
    return False

if __name__ == "__main__":
    main()