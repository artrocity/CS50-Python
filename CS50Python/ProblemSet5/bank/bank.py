def main():
    user_greeting = input("Greeting: ").strip().lower()
    #print output from value
    output = value(user_greeting)
    print(output)

#Determine the Value
def value(greeting):
    #Ignore any leading whitespace, case insensitively
    greeting = greeting.strip().lower()
    #Greeting starts with Hello = $0
    if greeting.startswith("hello"):
        output = "$0"
    #Greeting starts with H = $20
    elif greeting.startswith("h"):
        output = "$20"
    #Otherwise = $100
    else:
        output = "$100"
    return output

if __name__ == "__main__":
    main()



