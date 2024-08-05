# Chapter 1 - Programming Exercises

# 1 - Typing Commands

#print("Hello, world!") # Hello, world!
#print("Hello", "world!") # Hello world!
#print(3) # 3
#print(3.0) # 3.0
#print(2 + 3) # 5
#print(2.0 + 3.0) # 5.0
#print("2" + "3")
#print("2 + 3 =", 2 + 3)
#print(2 * 3)
#print(2 ** 3) #2^3 = 8
#print(7 / 3) # 2.3333333333333335 - divide with remainder
#print(7 // 3) # 2 - divide w/o remainder

# 3 -4: Chaos function tweaks
# The chaos function (logistic regression) changes with the change in equation because the function approximates to around 2...
# Looking at the function itself, it looks like
def chaos():
    x = eval(input("Enter number between 0 and 1: "))
    for i in range(20): # modify from 10 to 20
        x = 2 * x * (1 - x)
        print(x)

#chaos()

# 5. Modify chaos program so number of values to print is determined by user.
def chaotic():
    x = eval(input("Enter number between 0 and 1: "))
    n = eval(input("Pick how many times you want printed: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

# Invoke function
chaotic()

import math 
# Function Definition 
def function_name(parameters): 
    "functioninfo"
    # Define variables: function that returns the average of entered values 
    num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #num2 = [14, 15, 16, 17, 18] 

    a = len(num1)
    #b = len(num2) 

    average = num1 / a 

    return(average) 

# Run function 
    parameters() 

# Testing with other variables 
    testing = [25, 30, 35, 40, 45] 

    

    c = len(testing) 

    averageb = testing/c 

    
def is_leap(year):
    
    numbers = [1, 2, 3, 4, 5]
    values = len(numbers)
    #leap = False 
    return values  
    

# https://python-programming.quantecon.org/functions.html 
ts_length = 100

# empty list 
usd_values = []   

for i in range(ts_length):
    usd = np.random.randn()
    usd_values.append(usd)

plt.plot(usd_values)
plt.show()

def x_loop(a):
    a = 1
    for i in range(a):
        a = 2 * x
    return a

    

