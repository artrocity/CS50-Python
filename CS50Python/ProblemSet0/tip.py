def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    # Accept a str as input $##.##
    # Remove the Leading $
    d = d.replace("$", "")
    # Return the amount as a float
    return float(d)

def percent_to_float(p):
    # TODO
    # Accept a str as input ##%)
    # Remove the %
    p = p.replace("%", "")
    # Return the percentage as a float
    p = float(p) / 100
    return float(p)

main()