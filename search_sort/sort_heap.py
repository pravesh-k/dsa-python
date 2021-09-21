### HEAP SORT

##  Heap Sort is a sorting technique which employs two types of data structures- arrays and trees. The technique first builds
##  max heap out of the original array. A max heap's root is the largest element in the tree. Again translating the heap to
##  array, we get the root element at the start of the array and for ascending order sorting we need to put the largest 
##  element at the last position. Swapping the array[first] with array[last] does the job well. And now we need the 2nd 
##  largest element for which we take array[0 to last-1] and heapify it. This process continues till we get sorted array.

#   Time Complexity: Best: O(n log(n)) 
#   (Explanation- while building first heap from original array, height of heap is log(n)
#   swapping nodes can occur multiple times, at max, n/2 times. So at that stage (n/2)log(n) ~ nlog(n) is the complexity.
#   While sorting the array, and removing last element, again causes n times log(n) steps of node movement. Since above
#   two steps occur one after other, complexity is not multiplied and it remains in the order of n*log(n)).
#   Space Complexity/Auxiliary Space: O(1)

array = [64, 25, 12, 22, 11, 33, 2, 100, 111, 44]

def heapify(arr, n, i):

    largest = i         #last non-leaf parent assumed to be the largest to satisfy the condition of max heap
    left = 2*i+1        #left child of the any parent in a complete tree is given by this expression
    right = 2*i+2       #right child of the any parent in a complete tree is given by this expression

    if left<n and arr[left]>arr[largest]:       #find which child is larger than parent node
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    
                                                #if the parent was larger than any of its child than do nothing
    if largest != i:                            #but if found otherwise, (i.e. one of the child is larger than 
        arr[i], arr[largest] = arr[largest], arr[i]     #parent as well other child) then swap it with the parent
        heapify(arr, n, largest)                        #finally now arr[i] is the parent node and larger than both
                                                        #its child, apparently arr[largest] as a parent for another
                                                        #sub-tree might not be in a heap structure, so again perform
                                                        #heapify operation for that parent/subtree.

def heap_sort(arr):

    n = len(arr)

    for i in range((n//2)-1, -1, -1):               #heapify the original array, root node has the largest value
        heapify(arr, n, i)

    for i in range(n-1, -1, -1):                    #to sort the array using heap, swap the last element with the 
        arr[0], arr[i] = arr[i], arr[0]             #first element because first element is the root node (largest in array)
        heapify(arr, i, 0)                          #of heapified binary tree. Then again heapify the remaining array
                                                    #except last element

heap_sort(array)
print("Sorted array is\n", array)