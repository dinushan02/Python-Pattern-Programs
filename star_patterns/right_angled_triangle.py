# Right Angled Triangle Pattern

rows = 6

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
Output:
*
* *
* * *
* * * *
* * * * *
* * * * * *

Explanation:
rows = 6 → controls number of rows
outer loop (i) → controls number of lines
inner loop (j) → prints stars in each row
print() → moves cursor to next line after each row is printed

Why we use print():
Without print(), all stars would be printed in a single line.
With print(), each row starts on a new line, forming a proper triangle pattern.
"""