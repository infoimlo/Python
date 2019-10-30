# Chapter 5: Programming Exercises - pgs 171 - 174

# 1. Redo dateconvert2.py program
# dateconvert.py
# Converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # get date
    dateStr = input("Enter a date (mm/dd/yyy):")

    # Split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # Convert monthStr to month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October",
              "November", "December"]

    # Output result in month, day and year format
    print("The converted date is:", monthStr, dayStr + ",", yearStr)


#main()

# Example change2.py - pg 157
# Program to calculate value of some change in dollars
# Represents total cash in cents.
def change():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies * 1

    print("Your total is: ", total, "cents!")
    #print("The total value of your change is ${0}.{1: 0>2}".format(total//100, total%100)) # seems to produce an error - why?

# Invoke function
# change()

# Question 2: Write a program that accepts a quiz score as an input and prints out the corresponding grade.
# input - 1 integer
# output - 1 letter (text character: A - F)
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F

def quizGrade():
    quiz = int(input("Enter your quiz score as a number: "))

    if quiz is 5:
        print("Great job! Your letter grade is an A.")
    elif quiz is 4:
        print("Not bad...your letter grade is a B.")
    elif quiz is 3:
        print("Keep trying...your letter grade is a C.")
    elif quiz is 2:
        print("Not satisfactory. Your letter grade is a D.")
    else:
        print("Unfortunatly, you failed the quiz.")

# Invoke function
#quizGrade()

# Question 3: Write a program that accepts an exam score as an input and prints out the corresponding grade.
# 5 point quizes graded on scale: A: 90 - 100, B: 80 - 89, C: 70 - 79, D: 60 - 69, F: <60

# input: integer (exam score)
# output: letter grade (A - F)
# pseudo code: request student enter grade as number => program runs though grade => outputs corresponding letter grade

# Letter grades as list (sequence of letters)
grades = ['A', 'B', 'C', 'D', 'F']
#print(len(grades)) # 5

# Set letter grades
#A = range(90, 100)
A = list(range(90, 101))
#print(A)

B = list(range(80, 90))
#print(B)

C = list(range(70, 80))

D = list(range(60, 70))

# Anything less than D (60) = F
#F = list(range())

# Request grade as number
def score():
    numGrade = int(input("Enter your grade as a number: "))

    if numGrade in A:
        print("Congrats, your grade is an A!")
    elif numGrade in B:
        print("Not bad, your grade is a B.")
    elif numGrade in C:
        print("Your grade is pretty average as a C.")
    elif numGrade in D:
        print("Your grade isn't satisfactory as a D.")
    else:
        print("Please try harder. Your grade is an F.")

# Invoke function
#score()


#