from typing import *

# Requirement: Your solution should run in O(log n) time and O(1) space.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid == lo and mid == hi:
                return nums[mid]
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            mideven = (mid % 2 == 0)
            if nums[mid] == nums[mid-1] and mideven:
                hi = mid - 2
            elif nums[mid] == nums[mid-1] and (not mideven):
                lo = mid + 1
            elif nums[mid] == nums[mid+1] and mideven:
                lo = mid + 2
            else:
                hi = mid - 1
        print(mid)
        return nums[mid]
                
        
def main():
    s = Solution()

    input1 = [1,1,2,3,3,4,4,8,8]
    #input2 = [3,3,7,7,10,11,11]
    input2 = [1,1,2,2,4]

    output1 = s.singleNonDuplicate(input1)
    output2 = s.singleNonDuplicate(input2)


    print(input1, output1)
    print(input2, output2)

if __name__ == "__main__":
    main()
