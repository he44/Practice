from typing import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        pass


# 0 0 1
# 1 1 0
# 1 0 0

# 1. swap 1 and 2

# 1 1 0
# 0 0 1
# 1 0 0 

# 2. swap 2 and 3

# 1 1 0
# 1 0 0
# 0 0 1

# 3. swap 1 and 2

# 1 0 0
# 1 1 0
# 0 0 1

# greedy? DP?
