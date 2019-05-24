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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def print_first_text(records):
    incoming_number, answering_number, time = records[0]
    print(F"First record of texts, {incoming_number} texts {answering_number} at time {time}")
    pass

def print_last_call(records):
    incoming_number, answering_number, time, duration = records[-1]
    print(F"Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {duration} seconds")
    pass


print_first_text(texts)
print_last_call(calls)
