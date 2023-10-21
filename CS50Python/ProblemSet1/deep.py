# Ask user for input
meaning = input("What is the Answer to the Great Question of Life, The Univers, and Everything? ")

#Make input case insensitive and space insensitive
match meaning.lower().strip():
    case "42" | "forty two" | "forty-two" :
        print("Yes")
    case _:
        print("No")
