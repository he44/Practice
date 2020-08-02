from typing import *


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 7919  # 1000th prime number from wikipedia
        self.list = [[] for x in range(self.base)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        idx = key % self.base
        self.list[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.base
        for i in range(len(self.list[idx])):
            if self.list[idx][i] == key:
                self.list[idx].pop(i)
                break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.base
        return key in self.list[idx]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
# Add
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
