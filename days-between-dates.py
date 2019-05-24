# Given your birthday and current date, calculate age in days.
# Compensate for leap days.
# Assume bday and current date are correct.

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False

def daysInMonth(year, month):
    feb = 28
    if isLeapYear(year):
        feb = 29

    daysOfMonths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return daysOfMonths[month - 1]

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
    return (year, month, day)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    number_of_days = 0
    next_date = nextDay(year1, month1, day1)
    end_date = (year2, month2, day2)
    while next_date <= end_date:
        number_of_days += 1
        next_date = nextDay(next_date[0], next_date[1], next_date[2])
    return number_of_days


def testDaysBetweenDates():

    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


testDaysBetweenDates()
