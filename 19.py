# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        #  Move P2 n positions ahead
        for i in range(n):
            p2 = p2.next
        #  Move P1 and P2 together, when P2 hits last noted,
        #  P1 will hit the node before target
        if p2 is None:
            return p1.next
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        #  Deleting Nth Node from the end
        p1.next = p1.next.next
        return head