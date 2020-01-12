class Solution:
    def getNoZeroIntegers(self, n: int):
        #  try out all?
        for A in range(1, n):
            B = n - A
            if '0' not in str(B) and '0' not in str(A):
                return [A,B]
        return []

        
def main():
    s = Solution()
    inputs = [2, 11, 10000, 69, 1010, 0]
    for n in inputs:
        ans = s.getNoZeroIntegers(n)
        print(ans)


if __name__ == "__main__":
    main()
    
