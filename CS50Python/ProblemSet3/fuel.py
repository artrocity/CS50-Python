#prompt user for fraction
while True:
    u_input = input("Fraction: ")
    try:
        x_str,y_str = u_input.split("/")
        x = int(x_str)
        y = int(y_str)
        if y == 0:
            pass
        elif x > y:
            pass
        else:
            break
    except (ValueError, NameError, ZeroDivisionError):
        print("Invalid input.")


#Output Fraction, < 1 = E, >99 = F, else %
p = (x / y) * 100
rp = int(round(p))

if rp >= 99:
    print("F")
elif rp <= 1:
    print("E")
else:
    print(f"{rp}%")

