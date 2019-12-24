class Solution:
    def countAndSay(self, n: int) -> str:
        arr = [None] * (n+1)
        arr[1] = '1'
        for i in range(2, n+1):
            new_str = ''
            for char in arr[i-1]:
                new_str += ('1' + char)
            arr[i] = new_str
        return arr[n]


if __name__ == "__main__":
    s = Solution()
    for i in range(5):
        print(s.countAndSay(i+1))