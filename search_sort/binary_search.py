### BINARY SEARCH
##  Requires a sorted array
#   Time Complexity: O(log n) compared to time complexity of linear search is O(n)
#   Space Complexity: O(1) (for linear search as well)


lst = [2, 5, 9, 10, 19, 23, 34, 41, 45, 56, 88, 89, 98]
value = 9

def binary_search_iterative(lst, val):
    left_index = 0
    right_index = len(lst)-1

    while(left_index<=right_index):

        mid_index = (left_index+right_index)//2
        if lst[mid_index] == val:
            return mid_index
        elif val<lst[mid_index]:
            right_index = mid_index-1
        elif val>lst[mid_index]:
            left_index=mid_index+1
        else:
            return -1


def binary_search_recursive(lst, left_index, right_index, val):
    
    if left_index<=right_index:

        mid_index = (left_index+right_index)//2
        if lst[mid_index] == val:
            return mid_index
        elif val<lst[mid_index]:
            return binary_search_recursive(lst, left_index, mid_index-1, val)
        elif val>lst[mid_index]:
            return binary_search_recursive(lst, mid_index+1, right_index, val)


print("iterative method BS:", binary_search_iterative(lst, value))
print("recursive method BS:", binary_search_recursive(lst, 0, len(lst), value))