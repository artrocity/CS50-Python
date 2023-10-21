#Main Function of the program
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Checks if all Conditions have been met
def is_valid(s):
    return(
        is_alpha(s) and
        is_length(s) and
        is_alnum(s) and
        is_number(s)
    )
# Must start with 2 letters 
def is_alpha(s):
    if s[:2].isalpha():
        return True
    else:
        return False
#Checking Length min 2 max 6
def is_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False
#Checking for alpha numeric only
def is_alnum(s):
    if s.isalnum():
        return True
    else:
        return False
#Checking for numbers in the middle and if 0 is the 1st number
def is_number(s):
    has_n = False
    for i in range(2, len(s)):
        char = s[i]
        if char.isdigit():
            has_n = True
            if s[2] == "0":
                return False
        elif has_n:
            return False
    return True

main()