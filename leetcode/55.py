"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""


class Solution:
    """
    def canJump(self, nums):
        size = len(nums)
        dp = [False for x in range(size)]
        dp[-1] = True

        for i in range(size-2, -1, -1):
            far = min(size - 1, i + nums[i])
            for ni in range(i + 1, far):
                if dp[ni] == True:
                    dp[i] = True
                    break
            
        return dp[0]
    """

    def canJump(self, nums):
        size = len(nums)
        lm_good = size - 1

        for i in range(size - 2, -1, -1):
            if i + nums[i] >= lm_good:
                lm_good = i

        return (lm_good == 0)

                
            


            


def main():
    s = Solution()

    input_nums = [2,3,1,1,4]
    input_nums = [3,2,1,0,4]
    input_nums = [0,2,3]
    output = s.canJump(input_nums)
    print(output)


if __name__ == "__main__":
    main()

        
