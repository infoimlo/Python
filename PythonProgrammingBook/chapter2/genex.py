# General Exercises for Chapter 2

# Input, Process, Output (IPO)

# Objective: Design a program that converts celsius to fahrenheit

# Pseudocode
# Input the temperature in degrees Celsius (called celsius)
# Calculate the fahrenheit as (9/5) celsius + 32
# Output fahrenheit

def convert_tem():
    introduction = "The goal of this program is to seamlessless convert degrees Celsius into degrees Fahrenheit."
    print(introduction)
    celsius = eval(input("Enter today's temperature in degrees Celsius: "))
    # Convert c to f
    fahrenheit = (9/5) * celsius + 32

    print("Today's temperature is approximatly", fahrenheit, "degrees Fahrenheit.")

    # Input statement to give user chance to read results
    input("Press the Enter key to quit.")

# Invoke function
#convert_tem()


# Simultaneous Assignment
def main():
    print("This program computes the average of two exam scores.")

    # Set exam scores
    score1, score2 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:", average)

# Invoke function
#main()

# Get average of 3 test scores
# Input: store student's 3 test scores
# Output: print average of test scores
# Process: avg = x1 + x2 + x3 / n = 3

def testAvg():
    print("This nifty average grade calculator will do the number crunching for you so you can focus on your studies!")
    a, b, c = eval(input("Enter your three test results separated by a comma:"))
    avg = round((a + b + c) / 3, 2)
    print("You're average grade for this class is", avg, ".")
    print("Great job!")

# Invoke function
testAvg()

