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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def real_numbers_set(texts, calls):
    real_numbers = set()
    for info in texts: # add any texted number
        real_numbers.add(info[0])
        real_numbers.add(info[1])
    for info in calls:
        real_numbers.add(info[1]) # add called number
    return real_numbers

def telemarketers_set(real_numbers, calls):
    scammers = set()
    for info in calls:
        number = info[0]
        if number not in real_numbers:
            scammers.add(number)
    return scammers

def print_answer():
    real_numbers = real_numbers_set(texts, calls)
    scammers = telemarketers_set(real_numbers, calls)
    print("These numbers could be telemarketers: ")
    for number in sorted(scammers):
        print(number)
    pass


print_answer()
