#Prompt user for an arithmetic expression
calc = input("Expression: ")
x, y, z = calc.split(" ")

#Convert to floats
x1 = float(x)
z1 = float(z)

#Calculate the results
if y == "+":
    result = x1 + z1
    print(result)
elif y == "-":
    result = x1 - z1
    print(result)
elif y == "*":
    result = x1 * z1
    print(result)
elif y == "/":
    result = x1 / z1
    print(result)
else:
    print("Sorry, that function is not supported")



