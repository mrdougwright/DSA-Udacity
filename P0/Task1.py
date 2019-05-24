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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def count_uniq_phone_numbers(texts_and_calls):
    uniq_numbers = set()
    for info in texts_and_calls:
        n1 = info[0]
        n2 = info[1]
        uniq_numbers.add(n1)
        uniq_numbers.add(n2)
    return len(uniq_numbers)

def print_answer():
    data = texts + calls
    count = count_uniq_phone_numbers(data)
    print(F"There are {count} different telephone numbers in the records.")


print_answer()
