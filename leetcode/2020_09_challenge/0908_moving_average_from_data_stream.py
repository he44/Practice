from typing import *


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = [] 
        self.ma = 0
        self.count = size
        

    def next(self, val: int) -> float:
        # not enough vals
        if len(self.nums) < self.count:
            self.nums.append(val)
            old_count = len(self.nums) - 1
            remove = 0
        else:
            old_count = len(self.nums)
            remove = self.nums.pop(0)
            self.nums.append(val)
        self.ma = (self.ma * old_count - remove + val) / (len(self.nums))
        return self.ma
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))

