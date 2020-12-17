import numpy as np
input_name = "1_input_eg.txt"
input_name = "1_input.txt"

ACTIVE = "#"
INACTIVE = "."
NUM_CYCLE = 6

with open(input_name, "r") as fp:
    lines = fp.readlines()

initial_lx = len(lines)
initial_ly = len(lines[0]) - 1
initial_lz = 1
print("Initial dimension: {}, {}, {}".format(initial_lx, initial_ly, initial_lz))

end_lx = initial_lx + 2 * (NUM_CYCLE) #-1)
end_ly = initial_ly + 2 * (NUM_CYCLE) #-1)
end_lz = initial_lz + 2 * (NUM_CYCLE + 1)

# this is not accurate, I am just using arbitary large number to contain all relevant grid
# as there are only 6 cycles
end_lx = 21
end_ly = 21
end_lz = 21
xoff = 10
yoff = 10
zoff = 10

print("End dimension: {}, {}, {}".format(end_lx, end_ly, end_lz))
grid = np.zeros((end_lx, end_ly, end_lz), dtype=np.uint8)

active_cubes = set()
row = 0
for line in lines:
    col = 0
    for char in line.strip():
        if char == ACTIVE:
            active_cubes.add((row, col))
            grid[0 + zoff, row + zoff, col + yoff] = 1
        col += 1
    row += 1

print("Initial grid")
print(grid)

def bound(num, max_val):
    return (max(num-1, 0), min(num+2, max_val+1))

def check_grid(grid):
    new_grid = grid.copy()
    lx, ly, lz = grid.shape
    for x in range(lx):
        for y in range(ly):
            for z in range(lz):
                xbound = bound(x, lx)
                ybound = bound(y, ly)
                zbound = bound(z, lz)
                neighbor_active = np.sum(grid[
                    xbound[0]:xbound[1],
                    ybound[0]:ybound[1],
                    zbound[0]:zbound[1]
                    ]
                ) - grid[x,y,z]
                if grid[x,y,z] == 1:
                    if neighbor_active != 2 and neighbor_active != 3:
                        new_grid[x,y,z] = 0
                else:
                    if neighbor_active == 3:
                        new_grid[x,y,z] = 1
    return new_grid


lx, ly, lz = grid.shape
x = 1; y = 1; z = 1;
xbound = bound(x, lx)
ybound = bound(y, ly)
zbound = bound(z, lz)
neighbor_active = np.sum(grid[
    xbound[0]:xbound[1],
    ybound[0]:ybound[1],
    zbound[0]:zbound[1]
    ]
) - grid[x,y,z]
print(xbound, ybound, zbound)
print(grid[
    xbound[0]:xbound[1],
    ybound[0]:ybound[1],
    zbound[0]:zbound[1]
    ].shape)
print("Neighboar active:", neighbor_active)


for ci in range(NUM_CYCLE):
    grid = check_grid(grid)
    print(grid)

print(np.sum(grid))


