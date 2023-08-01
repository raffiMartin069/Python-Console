# Write a function that takes the base and height of a triangle and return its area.
#
# Examples
# tri_area(3, 2) ➞ 3
#
# tri_area(7, 4) ➞ 14
#
# tri_area(10, 10) ➞ 50

# Notes
# The area of a triangle is: (base * height) / 2
# Don't forget to return the result.

def toArea(x, y):
    return (x * y) // 2

base = int(input('Enter base: '))
height = int(input('Enter height: '))
print('Answer is: ' + str(toArea(base, height)))