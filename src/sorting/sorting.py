# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    # Your code here
    arrA_size = len(arrA)
    arrB_size = len(arrB)
    j = k = 0
    
    while j < arrA_size and k < arrB_size:
        
        if arrA[j] < arrB[k]:
            merged_arr[j + k] = arrA[j]
            j += 1
        else:
            merged_arr[j + k] = arrB[k]
            k += 1

    merged_arr[j+k:] = arrA[j:] + arrB[k:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # Your code here
    if len(arr) > 1:
        # divide array
        mid_index = len(arr) // 2
        # conquer the array
        return merge(merge_sort(arr[0:mid_index]), merge_sort(arr[mid_index:]))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

arrA = [1, 3, 5]
arrB = [0, 2, 3, 4, 15, 18, 20]
print(merge(arrA, arrB))

arr = [0, 15, 89, 3, 4, 2, 78, 12, 0]
print(merge_sort(arr))