import inflect
p = inflect.engine()


#Empty list variable
name_list = []

#Try the loop, except when EOF executed
try:
    while True:
            name = input("Name: ")
            name_list.append(name)
except EOFError:
    print()
    pass

#Join the list and output
adieu = p.join(name_list)
print(f"Adieu, adieu, to {adieu}")

