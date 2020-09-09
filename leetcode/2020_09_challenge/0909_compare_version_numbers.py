from typing import *


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_nums = version1.split('.')
        v2_nums = version2.split('.')
        l1 = len(v1_nums)
        l2 = len(v2_nums)
        for i in range(min(l1, l2)):
            v1 = int(v1_nums[i])
            v2 = int(v2_nums[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        if l1 > l2:
            for k in range(i+1, l1):
                v1 = int(v1_nums[k])
                if v1 > 0:
                    return 1
        elif l1 < l2:
            for k in range(i+1, l2):
                v2 = int(v2_nums[k])
                if v2 > 0:
                    return -1
        return 0
        
