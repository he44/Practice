from typing import *

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        from math import sqrt
        ds = DisjointSet(max(A))

        # for each number, it should be in the same group as all its factor (except 1)
        # this way using the factor we can link all elements with gcd > 1 into one group
        for num in A:
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    ds.union(num, factor)
                    ds.union(num, num // factor)

        # print(ds)

        ms = 0
        counter = {}
        for num in A:
            root = ds.find(num)
            if root not in counter:
                counter[root] = 1
            else:
                counter[root] += 1
            ms = max(ms, counter[root])

        return ms


# Following Algorithm Design Manual 6.1.3
# assuming elements will be 1, 2, ... n
class DisjointSet():

    # n: number of elements
    def __init__(self, n):
        # sentinel node at 0, so we don't have to modify index
        self.p = [-1 for i in range(n + 1)] # pointer to parent
        self.s = [1 for i in range(n + 1)] # size of subtree rooted at each node
        self.n = n # number of elements

    # find the root of tree containing element i
    def find(self, i):
        cur = i
        while self.p[cur] != -1:
            cur = self.p[cur]
        return cur

    # merge two subtrees
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.s[root_i] > self.s[root_j]:
                self.p[root_j] = root_i
                self.s[root_i] += self.s[root_j]
            else:
                self.p[root_i] = root_j
                self.s[root_j] += self.s[root_i]

    # check if same component
    def same_group(self, i, j):
        return self.find(i) == self.find(j)

    # def max_size(self):
        # ms = 0
        # for cs in self.s:
            # ms = max(ms,cs)
        # return ms

    def __repr__(self):
        s1 = "Parent pointers: " + str(self.p) + '\n'
        s2 = "Size attributes: " + str(self.s) + '\n'
        s3 = "Number of elements: "  + str(self.n) + '\n'
        return s1 + s2 + s3



def test_set():
    n = 6
    ds = DisjointSet(n)
    ds.union(2,4)
    ds.union(3,4)
    print(ds.find(2))
    print(ds.same_group(2,3))
    ds.union(1,3)
    print(ds.find(1))
    print(ds)

def test_problem():
    sol = Solution()
    cases = [
        [4,6,15,35],
        [20,50,9,63],
        [2,3,6,7,4,12,21,39]
    ]
    for A in cases:
        ans = sol.largestComponentSize(A)
        print(ans)


test_set()
#test_problem()
