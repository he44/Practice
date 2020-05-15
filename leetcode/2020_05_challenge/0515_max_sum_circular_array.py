from typing import *

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def maxSum(A):
            if len(A) == 0:
                return 0
            dp = [0 for x in range(len(A))]
            dp[0] = A[0]
            maxsum = dp[0]
            for i in range(1, len(A)):
                dp[i] = max(dp[i-1], 0) + A[i]
                maxsum = max(dp[i], maxsum)
            return maxsum
       
        c1 = maxSum(A)
        # switch the sign of A and find the minimum subarray
        # which cannot be empty 
        sumA = sum(A)
        mA1 = [-k for k in A[1:]]
        mA2 = [-k for k in A[:-1]]
        # signs switched, should be + not -
        c2 = sumA + maxSum(mA1)
        c3 = sumA + maxSum(mA2)
        #print(c1,c2,c3)
        return max(c1, c2, c3)

def main():
    s = Solution()
    A = [-2]
    print(s.maxSubarraySumCircular(A))

if __name__ == "__main__":
    main()
