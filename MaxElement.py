# Name: find_max_element
# Parameters: arr (an array of numbers)
# Returns: The maximum element in the array


from audioop import reverse
from unittest import removeResult
from unittest.util import sorted_list_difference


myList = []

maxPrompt = int (input("Number of elements: "))

# f is allows to embed expression inside literals || " ".
for i in range(maxPrompt):
    numCarry = int(input(f'{i + 1}.) First number: '))
    myList.append(numCarry)
    
    
# max function can be used
print(max(myList), min(myList))
