class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)
        

    def pop(self) -> None:
        if len(self.min_stack)*len(self.stack) == 0:
            return
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]



def main():
    print('hello wolrd')
    ms = MinStack()
    ms.push(3)
    print(ms.top(), ms.getMin())
    ms.push(4)
    print(ms.top(), ms.getMin())
    ms.push(3)
    print(ms.top(), ms.getMin())
    ms.pop()
    print(ms.top(), ms.getMin())


if __name__ == "__main__":
    main()