"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3 Week 4 (Functions)
"""
n = int(input("Enter a value for n: "))

def recursive_sum(num):
    # Base case: if num is 1, stop recursion
    if num == 1:
        return 1
    # Recursive case: add num to the sum of numbers before it
    else:
        return num + recursive_sum(num - 1)

result = recursive_sum(n)
print("The sum from 1 to", n, "is:", result)