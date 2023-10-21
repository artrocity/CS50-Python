import sys
from tabulate import tabulate

def main():
    get_arg(sys.argv)
    table, headers = format_file()
    #using ASCII art, output table in grid format
    print(tabulate(table, headers, tablefmt="grid"))


def get_arg(args):
    #if no input, exit
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too Many command-line arguments")
    #Doesn't end in csv, exit
    elif not args[1].endswith(".csv"):
        sys.exit("Not a CSV file")

def format_file():
    #empty lists for dictionary
    table = []
    headers = []
    #read the file #DictRead and Read
    try:
        #Format table using tabulate grid
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            headers = lines[0].strip().split(",")
            for line in lines[1:]:
                row = line.strip().split(",")
                table.append(row)

    #if file not found, Raise FileNotFoundError, exit
    except FileNotFoundError:
        sys.exit("File does not exist")
    return table, headers

if __name__ == "__main__":
    main()