import sys

def main():
    check_sys(sys.argv)
    print(line_check())

#Expects 1 command-line argument, the name or path of a python file.
def check_sys(arg):
    #If user does not specifiy one cli
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #file doesnt end in.py
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif len(sys.argv) == 2:
            return sys.argv

#Check lines of file
def line_check():
    total_lines = 0
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if line.lstrip().startswith("#") or line.isspace():
                    total_lines += 0
                else:
                    total_lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return total_lines

if __name__ == "__main__":
    main()



