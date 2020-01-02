"""
N-Queen problem
"""
import copy

class Solution:
    def check_prev(self, placed, r, j):
        ans = True
        for i in range(r):
            if placed[i] == j or placed[i] == j - (r-i) or placed[i] == j + (r-i):
                ans = False
        return ans

    
    def backtrack(self, placed, sol_set, r):
        n = len(placed)
        #  Base case (last row)
        if r == n:
            #  there should be a better way to do this
            #  i didn't understand how = works in python, apparently
            one_sol = copy.deepcopy(placed)
            sol_set.append(one_sol)
        #  Check each col
        sol = []
        for j in range(n):
            #  Check previous 
            if self.check_prev(placed, r, j):
                placed[r] = j
                #  Recursion
                self.backtrack(placed, sol_set, r+1)
                placed[r] = -1

    def leetcode_formating(self, row):
        n = len(row)
        f = []
        for r in range(n):
            line = ""
            for c in range(n):
                if c == row[r]:
                    line += 'Q'
                else:
                    line += '.'
            f.append(line)
        return f


    """
    @ param : n - number of queens, and dimension of the board
    @ return : list of all distinct solutions 
    """
    def solveNQueens(self, n):
        initial = [-1 for x in range(n)]
        solutions = []
        self.backtrack(initial, solutions, 0)
        #  Construct solutions to the ideal format
        formatted_sol = []
        for sol in solutions:
            formatted_sol.append(self.leetcode_formating(sol))
        return formatted_sol
        """
        for sol in formatted_sol:
            print(sol)
        return solutions
        """


def main():
    s = Solution()
    ans = s.solveNQueens(n=4)
    print(ans)


if __name__ == "__main__":
    main()
                    
