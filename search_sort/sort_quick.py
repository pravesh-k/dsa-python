### QUICK SORT
##  Quicksort is a sorting algorithm based on the divide and conquer approach. An array is divided into subarrays
##  by selecting a pivot element.The pivot element should be positioned in such a way that elements less than pivot
##  are kept on the left side and elements greater than pivot are on the right side of the pivot. 
##  The algorithm then performs the same process on each of the sub arrays
#   Time Complexity: Best: O(n log(n))(explanation: list/arr is being split in log(n) calls and
#   array partition takes linear time in each call)
#   Space Complexity/Auxiliary Space: O(n)


arr = [64, 25, 12, 22, 11, 33]

def quick_sort(arr):

    length = len(arr)
    if length <= 1:                             #base condition for recursive function.
        return arr
    else:
        pivot = arr.pop()                       #choosing last element of the array as the pivot element

    items_smaller = []
    items_greater = []

    for item in arr:
        if item > pivot:                        #all elements greater than pivot are appended to the items_greater sub-array
            items_greater.append(item)
        else:
            items_smaller.append(item)          #all elements equal to or smaller than pivot are appended to the items_smaller sub-array
        
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)      #calling quick_sort for the sub-arrays and returning
                                                                                #the quick sorted items_smaller and quick sorted 
                                                                                #items_greater along with the pivot point at correct position


print("Sorted array is\n", quick_sort(arr))


##  The above approach is not optimum as the auxiliary space required is O(n) due to usage of temporary sub arrays.
##  That implied, above solution is not an in-place algorithm. An in-place solution is such solution where we don't 
##  rely on temporary array and manipulation is done in the input array itself.
#   The approach used below to implement quick sort uses O(log(n)) auxiliary space due to call stack.

array = [64, 25, 12, 22, 11, 33]

def partition(arr, low, high):

    pivot = arr[high]

    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    # print("piv", i+1)
    return i + 1

def quick_sort_in_place(arr, low, high):

    if low<high:
        piv = partition(arr, low, high)
        
        # print("left", low, piv, high)
        quick_sort_in_place(arr, low, piv-1)
        # print("right", low, piv, high)
        quick_sort_in_place(arr, piv+1, high)


quick_sort_in_place(array, 0, len(array)-1)
print("Sorted array using optimized quick sort\n", array)