def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    grid = [list(line) for line in lines]

    prev_str = grid_to_str(grid)
    while True:
        update_grid(grid)
        new_str = grid_to_str(grid)
        if new_str == prev_str:
            break
        prev_str = new_str

    print("Equilibrium state")
    for row in grid:
        print(row)

    print("part 1:", count_occupied(grid))



def count_occupied(grid):
    h = len(grid)
    w = len(grid[0])
    ans = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "#":
                ans += 1
    return ans


def grid_to_str(grid):
    str_list = [''.join(row) for row in grid]
    return ''.join(str_list)


def update_grid(grid):
    h = len(grid)
    w = len(grid[0])
    def check_surrounding(r, c):
        irs = [-1, 0, 1]
        ics = [-1, 0, 1]
        ones = 0
        zros = 0
        for ir in irs:
            ur = r + ir
            for ic in ics:
                uc = c + ic
                if (ir == 0 and ic == 0) or (not 0 <= ur < h) or (not 0 <= uc < w):
                    continue
                if grid[ur][uc] == "L":
                    zros += 1
                elif grid[ur][uc] == "#":
                    ones += 1
        return ones, zros

    to_one = []
    to_zero = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == ".":
                continue
            ones, zros = check_surrounding(r,c)
            if grid[r][c] == "L" and ones == 0:
                to_one.append((r,c))
            if grid[r][c] == "#" and ones >= 4:
                to_zero.append((r,c))

    for r, c in to_one:
        grid[r][c] = "#"

    for r, c in to_zero:
        grid[r][c] = "L"




if __name__ == "__main__":
    main()
