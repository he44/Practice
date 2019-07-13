# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

class Solution:
    def sameChar(self, s_char, p_char):
        return (s_char == p_char or p_char == '.')
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        #  Set up the 2D array with sentinel row and column
        mem_match = []
        for r in range(s_len+1):
            mem_match.append([])
            for c in range(p_len+1):
                mem_match[r].append(False)
        #  When both string and pattern are empty, they match
        mem_match[0][0] = True
        #  When the second character of p is *, then it can match empty string
        for c in range(p_len):
            if p[c] == '*':
                mem_match[0][c+1] = mem_match[0][c-1]
        # if p[1] == '*':
        #     mem_match[0][1+1] = True
        #  Fill in the 2D array from top left to right bottom
        for si in range(s_len):
            for pi in range(p_len):
                if p[pi] != '*':
                    mem_match[si+1][pi+1] = mem_match[si][pi] and self.sameChar(s[si], p[pi])
                else:
                    #  Use the repetition 0 times, p[pi-1:pi] gives ''
                    t_0 = mem_match[si+1][pi-1]
                    #  Use the repetition (once, twice or even more)
                    #  remove one string that's identical to p[pi-1] from s
                    t_1 = mem_match[si][pi+1] and self.sameChar(s[si], p[pi-1])
                    mem_match[si+1][pi+1] = t_0 or t_1
        
        for i in range(s_len+1):
            for j in range(p_len+1):
                print(str(mem_match[i][j])[0], end=' ')
            print('')

        return mem_match[s_len][p_len]
        


def main():
    sol = Solution()
    ans = sol.isMatch('', '.*')
    print(ans)

    # print(sol.sameChar('a', 'a'))

if __name__ == "__main__":
    main()


"""
Dynamic Programming:
1.) What function, solving what problem?
- match(i, j): does string s[1...i] match the pattern p[1...j]
2.) In the end, we need match(len(s), len(p))
3.) Recursoin:
    How to get match(i,j) from match(i-1, j-1) or other sub problems
    at (i,j)
    - if p[j] is a normal lowercase letter, we can just regularly check
        match(i,j) == match(i-1, j-1) and (s[i] == p[j])
    - if p[j] is '.'
        we can have anything for s[i]
        match(i,j) == match(i-1, j-1)
    - if p[j] is '*'
        match(i,j) == match(i-1, j-1) and s[i] and p[j-1] match
            p[j-1] is lowercase letter
            p[j-1] is '.'
        I don't think it makes sense to have '**' in a regular expression pattern
4.) DP:
    now we just need to fill in this 2-D array iteratively
"""
