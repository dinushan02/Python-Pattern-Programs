# Inverted Right Angled Triangle Pattern

rows = 7

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
Output:
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

Explanation:
rows = 7 → controls number of rows
outer loop (i) → decreases from 7 to 1
inner loop (j) → prints stars in each row
print() → moves cursor to next line after each row is printed

Why we use print():
Without print(), all stars would be printed in a single line.
With print(), each row starts on a new line, forming a proper inverted triangle pattern.
"""