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