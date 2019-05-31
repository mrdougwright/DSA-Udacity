def nth_row_pascal(n):
    row = 11**n
    arr = []
    for char in str(row):
        arr.append(int(char))
    return arr

print(nth_row_pascal(0))
print(nth_row_pascal(1))
print(nth_row_pascal(2))
print(nth_row_pascal(3))
print(nth_row_pascal(4))
print(nth_row_pascal(6))
