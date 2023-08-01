# Write a function that takes an integer minutes and converts it to seconds.
#
# Examples
# convert(5) ➞ 300
#
# convert(3) ➞ 180
#
# convert(2) ➞ 120
# Notes
# Don't forget to return the result.

def toSeconds(x):
    return x * 60


myMin = int(input('Enter minutes: '))
print(toSeconds(myMin))