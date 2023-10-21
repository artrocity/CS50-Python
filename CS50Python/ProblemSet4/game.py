import random
import sys


#prompt user for a level, n - must be a positive number
while True:
    try:
        user_level = int(input("Level: "))
        if user_level > 0:
            break
    except:
        pass


#randomly choose an integer between 1 and the user selected lvl
secret_number = random.randint(1, user_level)
user_guess = None

#loop the function to check the following,
while user_guess != secret_number:
    try:
        user_guess = int(input("Guess: "))
#Guess must be positive
        if user_guess < 0:
            continue
#guess > number: Too small!
        elif user_guess < secret_number:
            print("Too small!")
            continue
#Guess < number: Too big!
        elif user_guess > secret_number:
            print("Too large!")
#Guess == Number: Just right! and exit program
        elif user_guess == secret_number:
            break
    except:
        pass

print("Just Right!")
sys.exit()