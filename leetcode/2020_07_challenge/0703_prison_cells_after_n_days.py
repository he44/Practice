from typing import *

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def cell_to_int(cells):
            res = 0
            for i in range(len(cells)-1, -1, -1):
                res += 2 ** (len(cells) - i) * cells[i]
            return res
        
        pattern = cell_to_int(cells)
        return pattern

        prev_cells = cells
        new_cells = [0 for x in range(len(cells))]
        for i in range(N):
            # so the first and last cells are always vacant
            for j in range(1, len(cells)-1):
                if prev_cells[j-1] == prev_cells[j+1]:
                    #print("1", i, j)
                    new_cells[j] = 1
                else:
                    #print("0", i, j)
                    new_cells[j] = 0
            # update
            prev_cells = new_cells[:]
            #print(i, new_cells, prev_cells)
        return new_cells


cases = [
    [[0,1,0,1,1,0,0,1], 2],
    [[0,1,0,1,1,0,0,1], 7]
]

sol = Solution()
for cells, N in cases:
    print(sol.prisonAfterNDays(cells, N))



        

