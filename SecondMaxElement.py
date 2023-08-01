# Name: find_second_max
# Parameters: arr (an array of integers)
# Returns: The second maximum element in the array


from multiprocessing.dummy import Array


def Process(threshold):

    myArray = []

    for i in range(threshold):
        n = int(input(f'{i + 1}.) Enter number: '))
        myArray.append(n) 
        
    return myArray

# Refactor function acquires maximum of array.
# stored in container then removed the max value.
# Check output by printing the whole array.
def Refactor(arr):

    maximum = arr
    container = maximum.remove(max(arr))
    return arr 

maxItem = int(input("Enter number of items: "))
display_Array = Process(maxItem)
new_List = Refactor(display_Array)
print('Second Largest Number is: ', max(new_List))







