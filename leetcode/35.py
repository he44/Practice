"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

class Solution:
    def searchInsert(self, nums, target) -> int:
        size = len(nums)
        #  no element / smaller than first element
        if size == 0 or target < nums[0]:
            return 0
        for i in range(size):
            if target == nums[i]:
                return i
            if target < nums[i]:
                return i
        #  larger than all elements
        return size


def main():
    s = Solution()
    nums = [1,3,5,6]
    targets = [5,2,7,0]
    for target in targets:
        output = s.searchInsert(nums, target)
        print(output)


if __name__ == "__main__":
    main()

        
