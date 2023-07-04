def isLeapYear(year):
    
    # A year is a leap year if it is evenly divisible by 4, 
    # but century years are not leap years unless they are evenly divisible by 400. 
    # This means that the year 2000 is a leap year, although 1900 is not.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
