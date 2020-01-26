# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        Method: 2 pointers
        A: a1 a2 c1 c2 c3
        B: b1 b2 b3 c1 c2 c3
        pa, pb each traverses one node at each step, however, they flow
        to the other list
        pa: a1 a2 c1 c2 c3 b1 b2 b3 c1 c2 c3
        pb: b1 b2 b3 c1 c2 c3 a1 a2 c1 c2 c3
        assuming len(A) = l(ua) + l(i)
        assuming len(B) = l(ub) + l(i)
        let pa travel: l(ua) + l(i) + l(ub) and let pb travel l(ub) + l(i) + l(ua)
        they will both be at the start of the intersectino
        Notice the implementation below is actually making each pointer go through l(ub) + l(ua) + l(i) + 1 steps
        This way it's made sure that they will both reach end at some point, for the loop to break (if no intersection)
        Might have infinite loop if write if not curA.next
        """
        curA, curB = headA, headB
        while curA != curB:
            curA = headB if not curA else curA.next
            curB = headA if not curB else curB.next
        return curA

                
        


        """
        Method: "truncating" the extra portion of the longer list
        E.g.
        A: a1 a2 c1 c2 c3
        B: b1 b2 b3 c1 c2 c3
        Start comparing b1 with a2, and so on
        
        Time: O(2n)?
        one round for length,
        one round for extra comparison
        """

        #  Grabbing the length of list A and list B
        curA, curB = headA, headB
        lenA = 0
        lenB = 0
        while curA is not None:
            lenA += 1
            curA = curA.next

        while curB is not None:
            lenB += 1
            curB = curB.next

        #  need to bring the longer one forward
        curA, curB = headA, headB
        if lenA > lenB:
            #  forward A 
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            #  forward B
            for i in range(lenB - lenA):
                curB = curB.next

        #  now if A and B have the reference, they are the intersectino?
        while curA != curB:
            curA = curA.next
            curB = curB.next

        #  if no intersection, curA will just be None
        return curA

