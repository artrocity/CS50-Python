import sys
import csv

def main():
    check_arg(sys.argv)
    before_csv = sys.argv[1]
    after_csv = sys.argv[2]
    data = old_csv(before_csv)
    new_csv(data, after_csv)

#Function to get Argv
def check_arg(arg):
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arg) > 3:
        sys.exit("Too many command-line arguments")

#Function to get old csv - Formatted last, first, house
def old_csv(filename):
    data = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

#Function to format old csv into new csv - Formatted first, last, house
def new_csv(data, filename):
    fieldnames = ["first", "last", "house"]
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            last_name, first_name = row["name"].split(", ")
            new_row = {
                "first": first_name,
                "last": last_name,
                "house": row["house"]
            }
            writer.writerow(new_row)

if __name__ == "__main__":
    main()

