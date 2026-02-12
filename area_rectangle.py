"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 1 Week 4 (Functions)
"""
def area(length, width):
# Add logic here
    return length * width
# Get values from user
length = float(input("Enter length: "))
width = float(input("Enter width: "))
# Call function and print result
print("Area =" , area(length, width))
