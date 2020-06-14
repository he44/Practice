from typing import *

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        

    def getKthAncestor(self, node: int, k: int) -> int:
        cur = node
        while k >= 0:
            cur = self.parent[cur]
            k -= 1
            if cur == -1:
                break
        return cur
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)





cases = [

]
sol = Solution()

for case in cases:
    pass
