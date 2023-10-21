class Jar:
    #Initialize a cookie jar with the given capacity
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Value Can not be negative")
        self.max_capacity = capacity
        self.current_capacity = 0

    #Return a string with n"🍪", if there are 3 cookies, str should return "🍪🍪🍪"
    def __str__(self):
        return "🍪" * self.current_capacity

    #Add n🍪 to the cookie jar.
    def deposit(self, n):
        #If adding that many exceeds capacity, raise ValueError
        if self.current_capacity + n > self.max_capacity:
            raise ValueError("This amount of cookies exceeds the maximum allowable limit")
        else:
            self.current_capacity += n

    #Remove n🍪 from jar. If there arent that many, then raise ValueError
    def withdraw(self, n):
        if self.current_capacity < n:
            raise ValueError("Insufficient Funds")
        else:
            self.current_capacity -= n

    #Return Cookie jars capacity. If capacity is a negative, return ValueError.
    @property
    def capacity(self):
        if self.max_capacity < 0:
            raise ValueError("Cookies can't be negative")
        return self.max_capacity

    #return the number of cookies in the jar
    @property
    def size(self):
        return self.current_capacity

def main():
    try:
        jar = Jar(0)
        print(f"Current Cookies: {jar}")
        print(f"Initial Size: {jar}")

        jar.deposit(10)
        print(f"Current Cookies: {jar.size}")

        jar.withdraw(5)
        print(f"Current Cookies: {jar.size}")

    except ValueError:
        print("Error:")


if __name__ == "__main__":
    main()