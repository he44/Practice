from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # trivial case: just one node
        if head == None or head.next == None:
            return head
        ehead = head.next
        ecur = ehead
        ohead = head
        ocur = head
        # ensuring the last ocur is valid, so that we can assign
        # ocur.next = ehead
        while ecur != None and ecur.next != None:
            # move odd
            ocur.next = ecur.next
            ocur = ocur.next
            # move even
            if ocur != None:
                ecur.next = ocur.next
                ecur = ecur.next
        ocur.next = ehead
        return head
            




        

def main():
    s = Solution()


if __name__ == "__main__":
    main()
        
