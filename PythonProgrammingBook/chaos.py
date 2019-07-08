# File: chaos.py
# Simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function!")

    # Chaos theory algorithm
    # Assign input to variable x
    x = eval(input("Enter a number between 0 and 1: "))
    # Create loop that runs 10 times
    for i in range(10):
        x = 3.9 * x * (1 - x) # looks like saving changes to x to x itself?
        print(x)

main()