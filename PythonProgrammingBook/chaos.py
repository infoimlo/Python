# File: chaos.py
# Simple program illustrating chaotic behavior.

# Pseduocode
# Program that mimiks the logistic function
# Takes an input as x
# manipultates input and returns a new x as output
# performs function 10 times to see how it changes over time

# Input: number between 0 & 1
# Output: manipulation of inputed number
# Process: x = 3.9 * x * (1 - x) performed 10 times

def main():
    print("This program illustrates a chaotic function!")

    # Chaos theory algorithm
    # Assign input to variable x
    x = eval(input("Enter a number between 0 and 1: ")) # use eval to convert string input to number (not safe online)
    # Create loop that runs 10 times
    for i in range(10):
        x = 3.9 * x * (1 - x) # looks like saving changes to x to x itself?
        print(x)

main()