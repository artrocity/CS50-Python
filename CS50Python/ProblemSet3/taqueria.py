#empty dict
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.0
#Prompts user for order one line at a time, until ctrl d,
while True:
    try:
        #Prompt User and make case sensitive
        item = input("Item: ").title()
        #Display menu price total, prefaced by $
        if item in menu:
            item_cost = menu[item]
            total += item_cost
            print(f"${total:.2f}")
        else:
            continue
    except EOFError:
        print(end="\n")
        break