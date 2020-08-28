from typing import *


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand7(self):
        import random
        return random.randint(1,7)

    def rand10(self):
        """
        :rtype: int
        """
        rmo = 41
        while rmo >= 40:
            row = self.rand7() - 1
            col = self.rand7() - 1
            rmo = row * 7 + col
        return rmo % 10 + 1



# normalize results: {1: 147, 2: 0, 3: 126, 4: 149, 5: 0, 6: 126, 7: 139, 8: 158, 9: 0, 10: 155}
# scaling results: {1: 142, 2: 0, 3: 155, 4: 126, 5: 139, 6: 0, 7: 157, 8: 0, 9: 136, 10: 145}


for num_7 in range(1, 8):
    num_10 = round((10 - 1) * (num_7 - 1) / (7 - 1)) + 1
    print("%d mapped to %d"%(num_7, num_10))

cases = [
    100000
]

sol = Solution()
for case in cases:
    counter = dict.fromkeys(range(1,11), 0)
    for i in range(case):
        num = sol.rand10()
        counter[num] += 1
    print(counter)
                                            
