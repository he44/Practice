from typing import *

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.chars = characters
        self.b = (1 << self.n) - (1 << self.n - self.k)
                

    def next(self) -> str:
        cur = [self.chars[j] for j in range(self.n) if self.b and (1 << self.n - j - 1)]
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1
        return ''.join(cur)
                

    def hasNext(self) -> bool:
        return (self.b > 0)
                        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
