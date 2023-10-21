import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    if match := re.findall(r"\bum\b" ,s, re.IGNORECASE):
        counter = len(match)
        return counter

if __name__ == "__main__":
    main()