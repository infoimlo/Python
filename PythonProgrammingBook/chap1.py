# Chapter 1.6

# Function/command - sequence of statements

# Define simple function w/o an argument
def hello():
    print("Hello")
    print("Computers are fun!")


# Invoke function
#hello()


# Design my own functions
def adder():
    a = 4
    b = 6
    return a + b

#print(adder())

def paste():
    x = [1, 2, 3, 4]
    y = 5

    for num in x:
       z = x.append(y)

    print(z)

#paste()


# Parameters/arguments - changeable parts in command

# Define simple function with a parameter/argument
def greet(person):
    print("Hello", person)
    print("How are you?")

# Invoke function
person = 'Loretta'
#greet(person)


# Personal project
# Function that displays user's age 10 years ago

# Input: current age
# Output: age 10 years ago
# Process: subtraction of years

# Pseudo code
# Message providing instructions for how user can interact with program
# Input: some whole number
# Process: younger = x - 10
# Output: Display x - 10

# Define function
def aging():
    print("The psychic will tell you how old you were ten years ago and how old you will be 10 years into the future! ")
    x = eval(input("Tell me your current age: "))
    y = x - 10
    z = x + 10
    print("Hmmm...ten years ago, you were", y, "years old!" )
    print("In ten years, you will be approximatly", z, "years old. You're very welcome. My gift comes from God!")

# Invoke function
#aging()

# Calculator for evaluating exponential function
# The calculator will take in a variable and spit out an evaluation for an exponential function.

# Input: variable x
# Output: manipulation of x as an addition with another variable
# Process: Print out of calculation evaluated 10 times

def calculate():
    x = 1, 2, 3, 4, 5
    y = 100, 90, 30, 60, 98.5

    for i in range(10):
        z = x + y
    print(z)


#invoke function
calculate()

# Hmmm...right now, all it does is contatenate the numbers as lists.
# Will have to fix later! 
