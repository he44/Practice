class Solution:
    def generateParenthesis(self, n: int):
        #  cur_sol: current parenthesis arrangement
        #  lmr: # of '(' - # of ')'
        def backtrack(cur_sol, lmr):
            #  one valid config
            if len(cur_sol) == n * 2:
                if lmr == 0:
                    ans.append(cur_sol)
                return
            if lmr < 0:
                return
            if lmr >= 0:
                backtrack(cur_sol + '(', lmr+1)
            backtrack(cur_sol + ')', lmr-1)
            return
        ans = []
        backtrack('', 0)
        return ans


def main():
    s = Solution()
    #  input
    n = 4

    #  result
    ans = s.generateParenthesis(n)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
        
