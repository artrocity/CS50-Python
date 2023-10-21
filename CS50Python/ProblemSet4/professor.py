import random

#Prompt user to solve each problem.
def main():
    #set score, total problems, and call get_level
    score = 0
    total_problems = 10
    level = get_level()

    #Start while loop
    for _ in range(total_problems):
        x, y, answer = generate_problem(level)
        correct = False

        #Try for 3 attempts, if no correct answer output EEE and show answer
        for _ in range(3):
            user_answer = int(input(f"{x} + {y} = "))
            try:
                if user_answer == answer:
                    score +=1
                    correct = True
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                pass
        if not correct:
            print(answer)
    print(score)

#Prompt user for a level, n. If level isnt 1,2,3 prompt again
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1,2,3]:
                break
        except ValueError:
            pass
    return n

#Returns randomly gnereated non-negative integer with level 1,2,3
def generate_problem(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)


    answer = x + y
    return x, y, answer


if __name__ == "__main__":
    main()