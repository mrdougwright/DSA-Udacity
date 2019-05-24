"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import re

def bangalore_area_code(number):
    return re.match('^\(080\)', number)

def area_code(number):
    return re.match('^\(.*\)', number)

def mobile_prefix(number):
    return re.match('^\d{4}', number)

def extract_area_code(number):
    code = area_code(number) or mobile_prefix(number)
    return code[0]

def bangalore_outbound_calls(calls):
    numbers_called = set()
    from_bangalore_count = 0
    to_bangalore_count = 0

    for call in calls:
        caller = call[0]
        called = call[1]
        if bangalore_area_code(caller):
            # key is called number, value is the caller from bangalore
            from_bangalore_count += 1
            numbers_called.add(called)

            if bangalore_area_code(called):
                to_bangalore_count += 1

    percent_within_bangalore = to_bangalore_count / from_bangalore_count

    return numbers_called, percent_within_bangalore

def print_answer():
    print("The numbers called by people in Bangalore have codes:")
    codes = set()
    list_of_calls, percent = bangalore_outbound_calls(calls)

    for number in sorted(list_of_calls):
        area_code = extract_area_code(number)
        if area_code not in codes:
            codes.add(area_code)
            print(area_code)

    percentage = round(percent * 100, 2)

    print(F"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
    pass


print_answer()
