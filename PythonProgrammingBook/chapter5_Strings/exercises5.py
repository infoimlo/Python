# Chapter 5: Programming Exercises - pgs 171 - 174

# 1. Redo dateconvert2.py program
# dateconvert.py
# Converts a date in form "mm/dd/yyyy" to "month day, year"

months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]

#print(months[11])

def main():
    '''
    Objective: User enters date as string mm/dd/yyyy
    Program separtes month, day, year
    Returns name of month only as string, day and year stay the same

    '''

    # Convert monthStr to month name - look up table
    months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]

    # get date
    datestr = input("Enter a date (mm/dd/yyy):")

    # Split into components
    monthstr, daystr, yearstr = datestr.split("/")

    # Convert text to integer
    month = int(monthstr)

    # Select name of month from list

    mon = month - 1

    # Make selection from string

    x = months[mon]

    # Return it
    print('The converted date is:', x, daystr, yearstr)

    #print(type(monthstr), type(daystr), type(yearstr))


    # Error - Converting whole list to one number - can't do that
    #x = int(months)

    # Output result in month, day and year format
    #print("The converted date is:", monthStr, daystr + ",", yearStr)


main()

