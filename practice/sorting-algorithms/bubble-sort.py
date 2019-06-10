# Bubble Sort
# In place sorting
# O(n^2)
# fmt: off
wakeup_times = [
  16, 49, 3, 12, 56, 49, 55, 22, 13,
  46, 19, 55, 46, 13, 25, 56, 9, 48, 45
]
# fmt: on


def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if this < prev:
                l[index] = prev
                l[index - 1] = this


bubble_sort_1(wakeup_times)
print(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if this_hour < prev_hour or (
                prev_hour == this_hour and this_min < prev_min
            ):
                l[index] = (prev_hour, prev_min)
                l[index - 1] = (this_hour, this_min)


bubble_sort_2(sleep_times)
print(sleep_times)
print(
    "Pass"
    if (
        sleep_times
        == [(21, 55), (21, 58), (22, 5), (23, 20), (24, 3), (24, 13), (24, 23)]
    )
    else "Fail"
)
