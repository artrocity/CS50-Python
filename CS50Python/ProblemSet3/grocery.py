#define empty dictionary
grocery_list= {}

#prompt user for items to add to list
while True:
    try:
        groceries = input("")

        if groceries in grocery_list:
            grocery_list[groceries] += 1
        else:
            grocery_list[groceries] = 1
    #Add until user inputs ctrl d
    except EOFError:
        break

#output grocery list in ALLCAPS, sorted alphabetically
for item, count in sorted(grocery_list.items()):
    print(f"{count} {item.upper()}")
