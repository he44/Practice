"""
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',

return the length of last word in the string.

(last word means the last appearing word if we loop from left to right)

If the last word does not exist, return 0.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        #  Base case, empty string
        if size == 0:
            return 0
        #  check the last character
        if s[-1] != " ":
            end = size
        else:
            end = None
        start = -1
        seen_char = False

        for idx in range(size-1, -1, -1):
            if s[idx] != " " and end is None:
                end = idx + 1
            if s[idx] == " " and end is not None:
                start = idx
                break
        print(start, end, size)
        if end is None:
            return 0
        #  s w1 w2 w3 e
        return (end - start - 1)


def main():
    s = Solution()
    inputs = ["a", "Hello World", " ", "       ", "b   a    "]
    for input_str in inputs:
        length = s.lengthOfLastWord(input_str)
        print(length)


if __name__ == "__main__":
    main()
        
