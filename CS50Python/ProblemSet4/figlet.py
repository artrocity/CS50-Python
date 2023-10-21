import sys
import random
from pyfiglet import Figlet

#store Figlet() in a variable called figlet
figlet = Figlet()
#Get fonts from figlet and store in value
rando = figlet.getFonts()
#Set Font Choice
font_choice = None

#0 = Random, 2 = Specific (-f or --F, must be a name of font), Anything else or invalid font --EXIT
if  len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--f"):
    font_choice = sys.argv[2]
    if font_choice not in rando:
        sys.exit("Invalid Usage")
elif len(sys.argv) == 1:
    font_choice = random.choice(rando)
else:
    sys.exit("Invalid Usage")

#Obtain User input
words = input("Input:")

#Set chosen font and output font
figlet.setFont(font=font_choice)
print(figlet.renderText(words))

