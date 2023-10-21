#Takes the users input
def main():
    smiles = input()
    endmsg = convert(smiles)
    print(endmsg)

#Converts emoticons to emojis
def convert(smiles):
    happy = smiles.replace(":)", "🙂")
    sad = happy.replace(":(", "🙁")
    return sad

main()




