#Amount Due
cost = 50

while cost > 0:
    print("Amount Due:", cost)
    payment = int(input("Insert Coin: "))
    if payment == 25 or payment == 10 or payment == 5:
        cost -= payment

change = abs(cost)
print("Change Owed:", change)

