class Solution:
    def permute(self, nums):
        return self.helper(0, nums)
    """
        helper(idx, nums) gives all permutations of the lists, returning list of lists
        if nums[0...idx-1] has been determined or nums[idx...n-1] is flexible
        so helper(0, nums) will give us the answer
        when idx == 0, we just return the entire list
    """
    def helper(self, last, nums):
        size = len(nums)
        #  base case
        if last == size:
            return [nums[:]]
        #  recursion, we can choose any number between nums[last:n-1]
        #  to sit at nums[last]
        outputs = []
        for k in range(last, size):
            #  choose a num
            nums[k], nums[last] = nums[last], nums[k]
            #  recursion
            outputs += self.helper(last+1, nums)
            #  backtrack
            nums[last], nums[k] = nums[k], nums[last]
        return outputs
        
        
        


def main():
    print("hello wolrd!")
    s = Solution()
    nums = [1,2,3]
    out = s.permute(nums)
    print(len(out))
    print(out)


if __name__ == "__main__":
    main()