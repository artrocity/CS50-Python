#Prompt user for string
def main():
    prompt = input("Input: ")
    print("Output: ", end="")
    rmv_vowels(prompt)

#Remove all Vowels
vowels = ["a","i","e","o","u"]

#create a function to remove vowels and output to main funct
def rmv_vowels(s):
    for c in s:
       #Make String lowercase
       if c.lower() not in vowels:
           print(c, end="")
    #Output String  
    print()

main()





