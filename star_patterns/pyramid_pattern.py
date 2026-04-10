# Pyramid Pattern (Simple Odd Star Pyramid)

for i in range(1, 11, 2):
    print("* " * i)

"""
Output:
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *

Explanation:
This pattern prints a simple pyramid using odd numbers.

range(1, 11, 2) → generates odd numbers (1, 3, 5, 7, 9)
i → controls number of stars in each row
"* " * i → prints stars based on current value of i
print() → moves cursor to next line after each row is printed

Why we use print():
Without print(), all stars would be printed in a single line.
With print(), each row starts on a new line, forming a pyramid structure.
"""