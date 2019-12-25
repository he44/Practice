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
    pass
    

#  Update the grid
def update_grid(grid):
    new_grid = [ [ 0 for i in range(5)] for j in range(5)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pass
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
    grid = read_input('eg_input.txt')
    #  grid = read_input('24_input.txt')
    num = grid_to_num(grid)
    visual_grid(grid)


if __name__ == "__main__":
    main()
