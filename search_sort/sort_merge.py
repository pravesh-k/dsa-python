### MERGE SORT
##  Merge Sort works on divide and conquer algorithm. We divide the input array into two halves and 
##  call the division again for the two halves and then merge the two halves post comparing
#   Time Complexity: Best: O(n log(n))(explanation: list/arr is being split in log(n) calls and
#   the merging process takes linear time in each call)
#   Space Complexity/Auxiliary Space: O(n)


arr = [64, 25, 12, 22, 11]

def merge_sort(arr):

    if len(arr)>1:
        mid_index = len(arr)//2     #finding the mid_index of the array

        L = arr[:mid_index]         #using temp arrays to store each of the array
        R = arr[mid_index:]
        
        merge_sort(L)               #recursive call to perform merge sort on left half as well as right half
        merge_sort(R)

        i = j = k = 0
        
                                        #merge operation:
        while i<len(L) and j<len(R):    #basically copying the elements from two halves to the array after comparision
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i<len(L):                 #copying the remaining elements from left half (if any)
            arr[k] = L[i]
            i += 1
            k += 1

        while j<len(R):                 #copying the remaining elements from right half (if any)
            arr[k] = R[j]
            j += 1
            k += 1


merge_sort(arr)
print("Sorted array is\n", arr)