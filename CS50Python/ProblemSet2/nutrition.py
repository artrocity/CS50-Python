#Create a Dictionary for fruit
#Key is the type of fruit, Value is the Calories
calorie_dict = {
    "Apple" : "130",
    "Avocado" : "50",
    "Banana" : "110",
    "Cantaloupe" : "50",
    "Grapefruit" : "60",
    "Grapes" : "90",
    "Honeydew Melon" : "50",
    "Kiwifruit" : "90",
    "Lemon" : "15",
    "Lime" : "20",
    "Nectarine" : "60",
    "Orange" : "80",
    "Peach" : "60",
    "Pear" : "100",
    "Pineapple" : "50",
    "Plums" : "70",
    "Strawberries" : "50",
    "Sweet Cherries" : "100",
    "Tangerine" : "50",
    "Watermelon" : "80"
}
#Define Main Function to check against dictionary
def main():
    #Prompt user to input a fruit, make case insensitive
    fruit = input("Item: ").title()
    if fruit in calorie_dict:
        value = calorie_dict[fruit]
        print(f"Calories: {value}")

main()
