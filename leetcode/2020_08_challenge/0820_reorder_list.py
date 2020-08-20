from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        # get index of each nodes
        as_arr = []
        cur = head
        while cur:
            as_arr.append(cur)
            cur = cur.next
        n = len(as_arr)
        # reorder
        temp = None
        for i in range(n // 2):
            temp = as_arr[i].next
            as_arr[i].next = as_arr[n - i - 1]
            as_arr[n - i - 1].next = temp
        # need to let go of the old "next" of the last node in the new list
        if temp:
            temp.next = None
        return head

 # 0 1 2
# [1,2,3]

# n = 3
# i = 0
 # temp = 2
 # 1 --> 3
 # 3 --> 2

# [1]
# n = 1
# i = 0
    # temp = None
    # 1 --> 1
