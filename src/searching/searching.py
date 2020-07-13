# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    # Your code here
    arr.sort()
    target_index = -1

    if start <= end:
        mid = ( start + end ) // 2

        if target == arr[mid]:
            target_index = mid
        elif target < arr[mid]:
           target_index = binary_search(arr, target, start, mid-1)
        elif target > arr[mid]:
            target_index = binary_search(arr, target, mid+1, end)  

    return target_index  # not found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

# Binary Search
arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr, -2, 0, 13))