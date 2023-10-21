#Prompt User for Greeting and strip it
greet = input("Greeting: ").lower().strip()

#Compare values
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")