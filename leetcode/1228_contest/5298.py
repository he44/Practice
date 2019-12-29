"""
Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result).
"""

class Solution:
    def isSolvable(self, words, result):
        #  find unique characters
        diff_chars = {}
        for i in range(len(words)):
            for c in words[i]:
                if c in diff_chars:
                    continue
                else:
                    diff_chars[c] = 0
        for c in result:
            if c in diff_chars:
                continue
            else:
                diff_chars[c] = 0
        num_diff_chars = len(diff_chars)
        #  Map a value to these chars
        #  i.e. "SEND" would mean 1000 * "S", 100 * "E" ...
        left_char_to_math = {}
        right_char_to_math = {}
        for char in diff_chars:
            left_char_to_math[char] = 0
            right_char_to_math[char] = 0

        #  Left side
        for word in words:
            size = len(word)
            for idx in range(size):
                left_char_to_math[word[idx]] += 10 ** (size - 1 - idx)

        #  Right side
        size = len(result)
        for idx in range(size):
            right_char_to_math[result[idx]] += 10 ** (size - 1 - idx)

        print(left_char_to_math)
        print(right_char_to_math)
        print(diff_chars)

        #  Eliminate the common ones
        equation = {}
        for key in left_char_to_math:
            equation[key] = left_char_to_math[key] - right_char_to_math[key]

        print("Solving this", equation)

        #  Brutal force ?

        
                
        

def main():
    print('hello world')
    words = ["SEND","MORE"]
    result = "MONEY"

    s = Solution()
    s.isSolvable(words, result)


if __name__ == "__main__":
    main()

        
        
