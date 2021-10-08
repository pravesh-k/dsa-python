## This problem is from LeetCode numbered #35. Search Insert Position

# Problem Statement: Given a sorted array of distinct integers and a
# target value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order. 
# (Time Complexity should be O(log n))

# Costraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums (the input array) contains distinct values in ascending order.
# -104 <= target <= 104


from typing import List

class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        
        first, last = 0, len(nums) - 1
        
        # if element is smaller than nums[first] then it should be inserted at 0-th position in nums
        if target < nums[first]:
            return 0
        # if element is greater than nums[last] then it should be inserted at n-th position in nums
        elif target > nums[last]:
            return last + 1
        # otherwise if target is already present or can be inserted between two elemets, 
        # perform search operation to get the position using binary technique. 
        else:
            while first <= last:

                mid = (first + last) // 2       # finding the mid position at each iteration

                # if element is present at mid position or if it can be placed at the mid, 
                # then return the mid position otherwise perform divide rule on array depending 
                # on the target's comparision with the mid element of the array
                if nums[mid] == target or (target < nums[mid] and target > nums[mid-1]):
                    return mid
                elif target < nums[mid]:
                    last = mid -1
                else:
                    first = mid + 1


# driver code
def main():

    sol = Solution()
    
    nums = [1,3,5,6]
    target = 2

    print(sol.searchInsert(nums, target))


if __name__ == "__main__":
    main()
