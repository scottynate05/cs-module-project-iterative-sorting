from math import floor

def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    n = len(arr)
    l = 0
    r = n -1 

    while l <= r:
        mid = floor((l + r) / 2)
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid -1
        else:
            return mid

    return -1  # not found
