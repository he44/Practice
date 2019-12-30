"""
1307. Verbal Arithmetic Puzzle

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result).

Idea: if the sum holds, all digits addition must hold as well.

E.g. SEND + MORE = MONEY

For this equation to hold, you must have "D" + "E"  = "Y" with an optional carry in bit

So we can start by assigning the values for all LSB and stop early if they won't fit

Reversing all the strings in this problem

DNES
EROM
YENOM

dp representation dp[c, r, s]
c - column (which bit)
r - row (which word)
s - carry-in sum from the previous column
dp[c,r,s] - if there's a way to satisfy the equation from column c, word r, and sum s from prevoius columns
"""



class Solution:
    def solve_helper(self, c, r, s, n2c, c2n, count_words, longest_word, rev_words, result):
        #  one column done, if works, move forward, if not, stop right here
        if r == count_words-1:
            #  if this one not mapped, map it and throw it into recursion
            if rev_words[r][c] not in c2n:
                for digit in range(10):
                    if digit not in n2c:
                        c2n[rev_words[r][c]] = digit
                        n2c[digit] = rev_words[r][c]
                        ans = (self, c, r, s, n2c, c2n, count_words, longest_word, rev_words, result)
                        if ans:
                            return True
                        else:
                            c2n.pop(rev_words[r][c])
                            n2c.pop(digit)
                return False
            else:
                #  calculate the sum after adding this column
                col_sum = s
                for ridx in range(count_words):
                    col_sum += c2n[rev_words[ridx][c]]
                col_digit = col_sum % 10
                #  check the digit on results
                if result[c] not in c2n:
                    if col_digit not in n2c:
                        c2n[result[c]] = col_digit
                        n2c[col_digit] = result[c]
                    else:
                        return False
                #  Move forward
                return self.solve_helper(c + 1, 0, col_sum // 10, n2c, c2n, count_words, longest_word, rev_words, result)

        #  If current character rev_words[c][r] is already mapped, or it's empty, move to the next one
        if c > len(rev_words[r]) or rev_words[c][r] in c2n:
            return self.solve_helper(c, r+1, s, n2c, c2n, count_words, longest_word, rev_words, result)
        else:
            #  If current character exists but hasn't been mapped
            #  if c <= len(rev_words[r]) and rev_words[c][r] not in c2n:
            #  try out all possible remaining values
            digit_range = range(10) if c != 0 else range(1,10)
            for digit in digit_range:
                if digit not in n2c:
                    n2c[digit] = rev_words[r][c]
                    c2n[rev_words[r][c]] = digit
                    ret = self.solve_helper(c, r + 1, s, n2c, c2n, count_words, longest_word, rev_words, result)
                    #  if works, great
                    if ret:
                        return True
                    #  if not, scratch off the pair and try the next one
                    else:
                        n2c.pop(digit)
                        c2n.pop(rev_words[r][c])
            #  if none of them works, it won't work right?
            return False
            
    
    def isSolvable(self, words, result):
        #  Number of words
        count_words = len(words)
        #  Length of longest word
        longest_word = 0
        for i in range(count_words):
            longest_word = max(longest_word, len(words[i]))
        #  if words have numbers with more digits than results, equation won't hold (no leading zeros)
        if longest_word > len(result):
            return False

        rev_words = [w[::-1] for w in words]
        n2c = {}
        c2n = {}
        ans = self.solve_helper(0, 0, 0, n2c, c2n, count_words, longest_word, rev_words, result)
        return ans

        

def main():
    print('hello world')

    """
    words = ["SEND","MORE"]
    result = "MONEY"
    """
    words = ["LEET","CODE"]
    result = "POINT"
    words = ["SIX","SEVEN","SEVEN"]
    result = "TWENTY"
    s = Solution()

    #  Reverse all the words with Python Slicing
    #  [start:end:increment], no number means start/end
    rev_words = [w[::-1] for w in words]
    print(rev_words)

    ans = s.isSolvable(words, result)
    print(ans)
    


if __name__ == "__main__":
    main()

        
        
