vowels = ["a","e","i","o","u"]

#Call on functions to output string
def main():
    txt = input("Input: ")
    print("Output: ", end="")
    print(shorten(txt))

#Remove all vowels from string
def shorten(word):
    short = ""
    for i in word:
        #Make input case insensitive/Remove all vowels
        if i.lower() not in vowels:
            short += i
    return short

if __name__ == "__main__":
    main()



