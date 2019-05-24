"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
import collections

def longest_phone_call(calls):
    list_of_calls = collections.defaultdict(int)
    longest_call = 0
    telephone_number = None

    # build call dictionary, with `number` as key and total `call_duration` as value.
    for info in calls:
        call_duration = int(info[3])

        for number in info[0:2]:
            list_of_calls[number] += call_duration
        # iterate through all numbers to find longest phone call.
        if list_of_calls[number] > longest_call:
            longest_call = list_of_calls[number]
            telephone_number = number

    return telephone_number, longest_call

def print_answer():
    telephone_number, total_time = longest_phone_call(calls)
    print(F"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
    pass


print_answer()
