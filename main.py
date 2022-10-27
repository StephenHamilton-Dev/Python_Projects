
# Recursive Binary Search Algorithm #

def binary_search(array, target, low, high):

    # check if element is in array
    if high >= low:

        midpoint = (low + high) // 2  # calculate midpoint in array

        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] > target:
            return binary_search(array, target, low, midpoint - 1)   # recurse through array and search left side
        elif array[midpoint] < target:
            return binary_search(array, target, midpoint + 1, high)  # recurse through array and search right side

    else:
        # if element is not in array
        return -1


# Test Array
array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Target we are looking for
target = 16

'''
call binary search function and set it equal to variable
pass in parameters and make low = 0, and high = len(array)-1
'''
result = binary_search(array, target, 0, len(array)-1)

if result != -1:
    print(f"Binary search found the target at index: {result}")
else:
    print("Target not found")

