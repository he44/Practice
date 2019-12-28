
def sum_col(grid, c):
    total = 0
    for r in range(5):
        total += grid[r][c]
    return total

def sum_row(grid, r):
    total = 0
    for c in range(5):
        total += grid[r][c]
    return total


#  Sum up the number of bugs in one grid
def sum_grid(grid):
    sum_g = 0
    for row in grid:
        sum_g += sum(row)
    return sum_g


def visual_grid(grid):
    print('+++++++++++++++++++++++++++')
    for row in grid:
        print(row)
    #  print(grid_to_num(grid))
    print('+++++++++++++++++++++++++++')

def main():
    grid = [[1 for x in range(5)] for y in range(5)]
    visual_grid(grid)
    grid[1][2] = 3
    visual_grid(grid)
    print("Sum over row 1 is %d"%sum_row(grid, 1))
    print("Sum over col 1 is %d"%sum_col(grid, 2))
    print("Sum over grid is %d"%sum_grid(grid))

if __name__ == "__main__":
    main()
