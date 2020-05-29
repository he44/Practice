from typing import *

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        res = [0, 1]
        k = 2
        for i in range(2, num + 1):
            if i == 2*k:
                res.append(1)
                k *= 2
            else:
                res.append(1 + res[i-k])
        return res


def main():
    s = Solution()
    for i in range(16 + 1):
        print(i, s.countBits(i))
        

if __name__ == "__main__":
    main()
