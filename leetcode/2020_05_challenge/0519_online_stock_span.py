from typing import *

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        # merging the prevising increasing element that's smaller than current element
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

    def __repr__(self):
        return str(self.stack)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

def main():
    ss = StockSpanner()


if __name__ == "__main__":
    main()
