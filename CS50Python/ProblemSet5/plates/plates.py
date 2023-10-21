def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


#Check validity of all plate checks
def is_valid(s):
    return (
        is_alpha(s) and
        is_length(s) and
        number_check(s) and
        is_alphanum(s)
            )

#All vanity plates must start with at least two letters
def is_alpha(s):
    if s[:2].isalpha():
        return True
    else:
        return False

#Vanit Plates between 2-6 chars.
def is_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

#Numbers cannot be used in the middle of a plate; they must come at the end.
#The first number used cannot be a ‘0’.
def number_check(s):
    has_number = False
    for i in range(2, len(s)):
        character = s[i]
        if character.isdigit():
            has_number = True
            if s[2] == "0":
                return False
        elif has_number:
            return False
    return True


##“No periods, spaces, or punctuation marks are allowed.”
def is_alphanum(s):
    if s.isalnum():
        return True
    else:
        return False




if __name__ == "__main__":
    main()

