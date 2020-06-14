from typing import *

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        book = {}
        for num in arr:
            if num in book:
                book[num] += 1
            else:
                book[num] = 1
        s_book = sorted(book, key = lambda x: book[x])

        print(s_book)
        removed = 0
        for i in s_book:
            if k-book[i] >= 0:
                removed += 1
                k-=book[i]
            else:
                break
        return len(s_book) - removed

        


cases = [
    [[2,1,1,3,3,3],3]
]
sol = Solution()

for case in cases:
    print(sol.findLeastNumOfUniqueInts(case[0], case[1]))
