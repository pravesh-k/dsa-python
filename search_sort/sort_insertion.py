### INSERTION SORT
##  Sorting is done by virtually splitting the array into a sorted and an unsorted part. 
##  Values from unsorted part are picked and placed at the correct position in the
##  sorted part. It's just like sorting the playing cards.
#   Time Complexity: Best case: O(n) and in Worst case: O(n^2)
#   Space Complexity/Auxiliary Space: O(1)


arr = [64, 25, 12, 22, 11]

def insertion_sort(arr):

    for i in range (1,len(arr)):    #traversing from 2nd element to end assuming that only 1st element is sorted part of the array
        
        key = arr[i]                #picking one element from unsorted part of the array

                                    #if key is smaller than few elements of unsorted array then moving
        j = i-1                     #all those greater elements by one position and then placing the key just 
        while j>=0 and key<arr[j]:  #next to the next smaller element in the array
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


insertion_sort(arr)
print("Sorted array is\n", arr)