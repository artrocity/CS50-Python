# Create a function to take user input in camel case
def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(camel)

# Create a function to snake_case the user inputted camelCase
def snake_case(s):
    for letters in s:
        if letters.isupper():
            print("_" + letters.lower(), end="")
        else:
            print(letters, end="")
    print()

main()