from typing import *

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # Copy last element in the list to target position
            # remove the last element in the list, remove target in the dict
            last_val = self.list[-1]
            target_idx = self.dict[val]
            # copy last val to target in the list
            self.list[target_idx] = last_val
            # replace the index of last val with target idx
            self.dict[last_val] = target_idx
            # remove target val in dict
            self.dict.pop(val)
            # remove last val from list (already copied)
            self.list.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.list)

    def __str__(self):
        return str(self.list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

r = RandomizedSet()
#print(r)
r.insert(0)
#print(r)
r.insert(1)
#print(r)
print("Before removing 0", r)
r.remove(0)
print("After removing 0", r)
r.insert(2)
print(r)
print("Before removing 1", r)
r.remove(1)
print("After removing 1", r)
print(r)
print(r.getRandom())
print(r)
