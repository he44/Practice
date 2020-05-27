from typing import *
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 0
        count = 0
        counts = [None for x in range(n * 2 + 1)]
        counts[n] = -1 # the beginning (-1 denotes no numbers counted)
        for i in range(n):
            num = nums[i]
            # update the count
            if num == 0:
                count -= 1
            else:
                count += 1
            # put in counts[], this only keeps the most left one
            if counts[count + n] is None:
                counts[count + n] = i
            else:
                #print(i, counts)
                maxlen = max(i - counts[count + n], maxlen)
        #print(counts)
        return maxlen

def main():
    s = Solution()
    cases = [
        [0,1],
        [0,1,0],
        [0,0,1,0,0,0,1,1],
        [0,1,0,1]
    ]
    for case in cases:
        print(s.findMaxLength(case))


if __name__ == "__main__":
    main()
        
