"""
Description:

Given an array of non-negative integers arr, 
you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], 
check if you can reach to any index with value 0.

"""

class Solution:
    """
    @ param : arr - list of integers
    @ param : start - starting index
    @ return : bool
    """
    def canReach(self, arr, start):
        #  easy case, start is target
        if arr[start] == 0:
            return True
        #  initialization
        length = len(arr)
        visited_dp = {} 
        
        #  exploring until no more places to go?
        cur = start
        to_explore = [cur]
        while len(to_explore) != 0:
            #  BFS
            cur = to_explore.pop(0)
            if cur in visited_dp:
                continue
            else:
                visited_dp[cur] = 1
            #  adding possible location
            pos1 = cur + arr[cur]
            pos2 = cur - arr[cur]
            #  Adding pos1 to list
            if pos1 >= 0 and pos1 < length:
                to_explore.append(pos1)
                if arr[pos1] == 0:
                    return True
            #  Adding pos2 to list
            if pos2 >= 0 and pos2 < length:
                to_explore.append(pos2)
                if arr[pos2] == 0:
                    return True
        return False
        







"""
the path is not necessarily reversible
"""
