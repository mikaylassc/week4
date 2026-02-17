"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4 Week 4 (Functions)
"""
# Your list (array)
numbers = [4, 7, 1, 9, 3]

def find_max_min(num_list):
    # This function finds and prints the largest and smallest numbers in a list
    largest = max(num_list)
    smallest = min(num_list)
    print("Largest number:", largest)
    print("Smallest number:", smallest)
# Call the function
find_max_min(numbers)