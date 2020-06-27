from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None

        k = len(lists)
        
        while True:

            min_cur = float('inf')
            min_idx = -1

            # O(k) find smallest current node
            for i in range(k):
                if lists[i] and lists[i].val < min_cur:
                    min_cur = lists[i].val
                    min_idx = i

            if min_idx == -1:
                break

            print(min_cur, min_idx)

            # fix 
            if head == None:
                head = lists[i]
            else:
                head.next = lists[i]
                head = head.next
            lists[i] = lists[i].next

        return head


            

