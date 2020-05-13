from typing import *
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while len(stack)!=0 and k > 0 and int(stack[-1]) > int(d):
                stack.pop()
                k -= 1
            stack.append(d)
        #  we have more digits to remove
        #  all the digits left in the stack are larger than its left neighbors
        #  thus, we should start removing the remaining from the right
        #  e.g. "12345", 1, the stack would be ["1", "2", "3", "4", "5"]
        #  we didn't remove any digit, but all digits on stack are larger than it's left neighbor
        #  thus, we need to remove from the right
        if k:
            stack = stack[:-k]
            
        res = ''.join(stack).lstrip('0')
        if res == '':
            res = '0'
        return res
            
                
    

def main():
    s = Solution()
    inputs = [
        ("1432219", 3),
        ("10200", 1),
        ("10", 2),
        ("2345434", 3),
        ("1000000", 1),
        ("1000000", 0),
        ("9", 1),
        ("12345", 1)
    ]

    for num, k in inputs:
        print(num, k, s.removeKdigits(num, k))
        

if __name__ == "__main__":
    main()
        
