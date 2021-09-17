### BUBBLE SORT
##  Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order
#   Time Complexity: Best: O(n), Worst: O(n^2)
#   Space Complexity/Auxiliary Space: O(1)


arr = [64, 25, 12, 22, 11, 33]

# function for bubble sort
def bubble_sort(arr):
    
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swapping elements

bubble_sort(arr)
print("Sorted array is", arr)