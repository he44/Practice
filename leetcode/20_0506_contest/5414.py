from typing import *

class Solution:
    # won't pass the time limit
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # True if cl2 is subset of cl2
        def subset(cl1, cl2):
            for item in cl1:
                if item not in cl2:
                    return False
            return True

        # compare every pair
        nosubsets = [True for x in favoriteCompanies]
        for pi in range(len(favoriteCompanies)):
            for pj in range(len(favoriteCompanies)):
                if pi == pj:
                    continue
                if subset(favoriteCompanies[pi], favoriteCompanies[pj]):
                    nosubsets[pi] = False

        # print(nosubsets)
        # print(subset(favoriteCompanies[2], favoriteCompanies[0]))

        # result
        res = []
        for i in range(len(nosubsets)):
            if nosubsets[i]:
                res.append(i)
                
        return res

        
#  Note: to pass the time limit, do not hardcode subset() funciotn
#  use the python set function x.issubset(y) where x and y are both sets
#  if set(favoriteCompanies[pi]).issubset(set(favoriteCompanies[pj])):
        
