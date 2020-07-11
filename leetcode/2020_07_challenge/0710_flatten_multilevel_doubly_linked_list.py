from typing import *

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        stack = [head]
        prev = None
        while stack:
            cur = stack.pop()
            if prev:
                prev.next = cur
            cur.prev = prev
            # right subtree
            if cur.next:
                stack.append(cur.next)
            # left subtree
            if cur.child:
                stack.append(cur.child)
                cur.child = None

            prev = cur
        return head

