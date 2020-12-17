import numpy as np
input_name = "1_input_eg.txt"
input_name = "1_input.txt"

ACTIVE = "#"
INACTIVE = "."
NUM_CYCLE = 6

with open(input_name, "r") as fp:
    lines = fp.readlines()


# this is not accurate, I am just using arbitary large number to contain all relevant grid
# as there are only 6 cycles
end_lx = 21
end_ly = 21
end_lz = 21
end_lw = 21
xoff = 9
yoff = 9
zoff = 9
woff = 9

grid = np.zeros((end_lz, end_lw, end_lx, end_ly), dtype=np.uint8)

row = 0
for line in lines:
    col = 0
    for char in line.strip():
        if char == ACTIVE:
            print(char, row, col)
            print(row + xoff, col + yoff)
            grid[0 + zoff, 0 + woff, row + xoff, col + yoff] = 1
        col += 1
    row += 1

print("Initial grid: ")
print(grid[zoff, woff, :, :])

def bound(num, max_val):
    return (max(num-1, 0), min(num+2, max_val+1))

def check_grid(grid):
    new_grid = grid.copy()
    lz, lw, lx, ly = grid.shape
    for z in range(lz):
        for w in range(lw):
            for x in range(lx):
                for y in range(ly):
                    this_val = grid[z,w,x,y]
                    xbound = bound(x, lx)
                    ybound = bound(y, ly)
                    zbound = bound(z, lz)
                    wbound = bound(w, lw)
                    neighbor_active = np.sum(grid[
                        zbound[0]:zbound[1],
                        wbound[0]:wbound[1],
                        xbound[0]:xbound[1],
                        ybound[0]:ybound[1],
                        ]
                    ) - this_val
                    if this_val == 1:
                        if neighbor_active != 2 and neighbor_active != 3:
                            new_grid[z, w, x,y] = 0
                    else:
                        if neighbor_active == 3:
                            new_grid[z,w,x,y] = 1
    return new_grid




for ci in range(NUM_CYCLE):
    grid = check_grid(grid)
    print("Done with cycle {}".format(ci+1))

print(np.sum(grid))


