# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.

class Solution:
    def twoSum(self, nums, target):
        #  can't do the two pointer thing because the array is not sorted
        dict = {}
        for i in range(len(nums)):
            dict[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in dict and dict[nums[i]] != i:
                return [i, dict[nums[i]]]

        
        
