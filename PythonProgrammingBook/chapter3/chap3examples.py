# Program to calculate value of some change in dollars

def changeCount():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickles = eval(input("Nickles: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    print()
    print("The total value of your change is $", total)

# invoke function
#changeCount()

# Data types - int vs float
#print(type(3)) # <class 'int'>
#print(type(5.08)) # <class 'float'>
#print(type('Hey - sup!')) # <class 'str'>

# Check out how results are converted implicitly (int vs. float)
#print(type(3 + 4)) # <class 'int'>

# Program to calculate factorials
def factorialProcessor():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

# run/invoke function
factorialProcessor()