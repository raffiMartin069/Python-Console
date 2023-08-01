# Create a function that takes a number as an argument, increments the number by +1 and returns the result.
#
# Examples
# addition(0) ➞ 1
#
# addition(9) ➞ 10
#
# addition(-3) ➞ -2
# Notes
# Don't forget to return the result.

def toIncrement(x):
    return x + 1


myValue = int(input('Enter a value: '))
print(toIncrement(myValue))