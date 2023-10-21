#Prompt user for Mass as Integer in KG
# E(Joules) = M(Mass, Kg) * C(Speed of Light) ** 2
m = int(input("m: "))
c = 300_000_000
e = m * c ** 2

#Output the equivalent number of Joules as an Integer
print(f"E: {e}")