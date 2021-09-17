### SELECTION SORT
##  Sorting is done by repeatedly finding the minimum element in the array and putting it at the beginning.
#   Time Complexity: O(n^2)
#   Space Complexity/Auxiliary Space: O(1)


arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index]>arr[j]:
            min_index = j

    arr[min_index], arr[i] = arr[i], arr[min_index]

print("Sorted array is", arr)