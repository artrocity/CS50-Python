def main():
    fraction = input("Fraction: ")
    output = gauge(convert(fraction))
    print(output)

def convert(fraction):
    while True:
        try:
            #expects a str in X/Y format as input
            x_str, y_str = fraction.split("/")
            #ensure x and y are an integer
            x = int(x_str)
            y = int(y_str)
            #if X is greater than Y, then convert should raise a ValueError.
            if x > y:
                pass
            #if x > y:
            elif y == 0:
                pass
            else:
                break
        except (ValueError, TypeError, ZeroDivisionError):
            print("Error")
            pass
    percentage = (x / y) * 100
    rp = int(round(percentage))
    print(rp)
    return rp

def gauge(percentage):
    #"E" if that int is less than or equal to 1
    if percentage <= 1:
        total = "E"
    #"F" if that int is greater than or equal to 99,
    elif percentage >= 99:
        total = "F"
    #"Z%" otherwise, wherein Z is that same int.
    else:
        total = f"{percentage}%"
    return total

if __name__ == "__main__":
    main()