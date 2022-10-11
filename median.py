"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
#print(numbers)

#list with odd number of elements
if len(numbers)%2 == 1:
    medianIndex = math.ceil(len(numbers)/2) -1
    sortedList = sorted(numbers)
    median = sortedList[medianIndex]
    print (median)

#List with even number of elements
if len(numbers)%2 == 0:
    halfway = math.floor( len(numbers)/2 )
    sortedList = sorted(numbers)
    median = (sortedList[halfway-1] + sortedList[halfway]) / 2
    print (median)
