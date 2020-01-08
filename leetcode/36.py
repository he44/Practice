"""
36 Valid Sudoku

"""

class Solution:
    def isValidSudoku(self, board) -> bool:
        dim = 9
        #  check each row
        for row in range(dim):
            seen = {}
            for col in range(dim):
                tile = board[row][col]
                if tile == ".":
                    continue
                if tile in seen:
                    return False
                else:
                    seen[tile] = 1
        #  check each column
        for col in range(dim):
            seen = {}
            for row in range(dim):
                tile = board[row][col]
                if tile == ".":
                    continue
                if tile in seen:
                    return False
                else:
                    seen[tile] = 1
        #  check each three by three
        #  (idx, r, c)
        #  (0, 0, 0) (1, 0, 3) (2, 0, 6)
        #  (3, 3, 0) (4, 3, 3) (5, 3, 6)
        #  (6, 6, 0) (7, 6, 3) (8, 6, 6)
        for idx in range(dim):
            rs = (idx // 3) * 3
            cs = (idx % 3) * 3
            seen = {}
            for rr in range(0,3):
                for cc in range(0,3):
                    tile = board[rs+rr][cs+cc]
                    if tile == ".":
                        continue
                    if tile in seen:
                        return False
                    else:
                        seen[tile] = 1
        return True



def main():
    s = Solution()

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    output = s.isValidSudoku(board)
    print("Answer is", output)


if __name__ == "__main__":
    main()
