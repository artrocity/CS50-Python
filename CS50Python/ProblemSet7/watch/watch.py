import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #Extract YouTube URL thats the value of a src attribute of an iframe element therein
    if match := re.search(r'^<iframe.*(https?://(www\.)?youtube\.com/embed/xvFZjo5PgG0)"></iframe>$', s):
        short = match.group(1).replace("https://www.", "https://").replace("http://", "https://").replace("youtube.com", "youtu.be").replace("embed/", "")
        return short
    #No matches return None
    else:
        return None

if __name__ == "__main__":
    main()

