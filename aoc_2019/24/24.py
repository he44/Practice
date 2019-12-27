"""
Formulation
a scan of the entire area fits into a 5x5 grid (your puzzle input). The scan shows bugs (#) and empty spaces (.).

each tile updated every minute, simultaneously (counting for all first, then changing)

Maybe need some bit operation: 25-bit number

This way, it's easy to check if two layours are the same
"""


#  Return the 2-D list
def read_input(file_path):
    grid = [ [ 0 for i in range(5)] for j in range(5)]
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            if line[j] == '#':
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid
        
#  Convert grid to a number
#  following the definition of biodiversity
def grid_to_num(grid):
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            power = i * 5 + j 
            #  print(i, j, power, 2 ** power)
            if grid[i][j] == 0:
                continue
            num += 2 ** (power)
    return num

#  Count adjacent bugs
def count_in_adjacent_tiles(grid, i, j):
    count = 0
    h = len(grid)
    w = len(grid[0])
    #  top neighbor
    if i - 1 >= 0:
        count += int(grid[i-1][j] == 1)
    #  left neighbor
    if j - 1 >= 0:
        count += int(grid[i][j-1] == 1)
    #  right neighbor
    if j + 1 < w:
        count += int(grid[i][j+1] == 1)
    #  bottom neighbor
    if i + 1 < h:
        count += int(grid[i+1][j] == 1)
    return count
    

#  Update the grid
def update_grid(grid):
    new_grid = [ [ 0 for i in range(5)] for j in range(5)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #  A bug dies (becoming an empty space)
            #  unless there is exactly one bug adjacent to it.
            if grid[i][j] == 1 and count_in_adjacent_tiles(grid, i, j) != 1:
                new_grid[i][j] = 0
            #  An empty space becomes infested with a bug
            #  if exactly one or two bugs are adjacent to it.
            elif grid[i][j] == 0 and count_in_adjacent_tiles(grid, i, j) in (1,2):
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = grid[i][j]
    return new_grid
            
#  Visualize the grid
def visual_grid(grid):
    print('+++++++++++++++++++++++++++')
    for row in grid:
        print(row)
    print(grid_to_num(grid))
    print('+++++++++++++++++++++++++++')
            


def main():
    minute = 0
    #  grid = read_input('eg_input.txt')
    grid = read_input('24_input.txt')
    num = grid_to_num(grid)
    visual_grid(grid)
    new_grid = grid
    seen_numbers = {}
    while True:
        minute += 1
        if minute % 100 == 0:
            print(minute)
        new_grid = update_grid(new_grid)
        new_num = grid_to_num(new_grid)
        if new_num in seen_numbers:
            print('Done!')
            visual_grid(new_grid)
            break
        seen_numbers[new_num] = 1


if __name__ == "__main__":
    main()
