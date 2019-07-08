# Chapter 1.6

# Function/command - sequence of statements

# Define simple function w/o an argument
def hello():
    print("Hello")
    print("Computers are fun!")


# Invoke function
hello()


# Design my own functions
def adder():
    a = 4
    b = 6
    return a + b

print(adder())

def paste():
    x = [1, 2, 3, 4]
    y = 5

    for num in x:
       z = x.append(y)

    print(z)

paste()


# Parameters/arguments - changeable parts in command

# Define simple function with a parameter/argument
def greet(person):
    print("Hello", person)
    print("How are you?")

# Invoke function
person = 'Loretta'
greet(person)