import sys

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        #  Sorting the list
        sorted_nums = sorted(nums)
        size = len(nums)
        #  Initialize the min_dist(detremining if closest) and the outcome
        min_dist = sys.maxsize
        closest_sum = 0
        #  Iterate through combinations
        for left in range(size):
            mid = left + 1
            right = size - 1
            while mid < right:
                temp_sum = sorted_nums[left] + sorted_nums[mid] + sorted_nums[right]
                temp_dist = abs(temp_sum - target)
                # print(left, mid, right, temp_sum, temp_dist)
                #  Perfect match
                if temp_dist == 0:
                    return temp_sum
                #  Update the answer
                if temp_dist < min_dist:
                    # print(left, mid, right)
                    min_dist = temp_dist
                    closest_sum = temp_sum
                #  Go looking for new combos
                if temp_sum > target:
                    right -= 1
                else:
                    mid += 1
        return closest_sum