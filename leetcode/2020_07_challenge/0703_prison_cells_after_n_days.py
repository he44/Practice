from typing import *

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # convert a cell configuration to an integer
        def cell_to_int(cells):
            res = 0
            for i in range(len(cells)-1, -1, -1):
                res += 2 ** (len(cells) - i - 1) * cells[i]
            return res

        def update_cells(cells):
            new_cells = [0 for x in range(len(cells))]
            for j in range(1, len(cells) - 1):
                new_cells[j] = 1 if cells[j-1] == cells[j+1] else 0
            return new_cells

        seen = {}
        new_cells = cells
        i = 0
        while i < N:
            i += 1
            new_cells = update_cells(new_cells)
            new_cells_pattern = cell_to_int(new_cells)
            if new_cells_pattern in seen:
                cyc_len = i - seen[new_cells_pattern]
                num_cycs = (N - i) // cyc_len
                i += num_cycs * cyc_len
            else:
                seen[new_cells_pattern] = i

        return new_cells



cases = [
    [[0, 1, 0, 1, 1, 0, 0, 1], 7]#,
    # [[0, 1, 0, 1, 1, 0, 0, 1], 14],
    # [[0, 1, 0, 1, 1, 0, 0, 1], 15],
    # [[0, 1, 0, 1, 1, 0, 0, 1], 100],
    # [[0, 1, 0, 1, 1, 0, 0, 1], 100000],
    # [[1, 0, 0, 1, 0, 0, 1, 0], 1000000000]
]

cases = [
    [[0, 0, 0, 1, 1, 0, 1, 0], 574]
]

sol = Solution()
for cells, N in cases:
    print(sol.prisonAfterNDays(cells, N))



        

