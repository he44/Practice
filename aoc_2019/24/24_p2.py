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
    #  print(grid_to_num(grid))
    print('+++++++++++++++++++++++++++')

#  Sum up the number of bugs in one grid
def sum_grid(grid):
    sum_g = 0
    for row in grid:
        sum_g += sum(row)
    return sum_g

#  Update all grids
#  prev_grids: a dictionary of all the possible grids
def update_all_grids(prev_grids, minutes, current_minute):
    #  for current_minute, only 2 * current_minute + 1 grids need to be udpated
    for i in range(minutes - current_minute, minutes + current_minute + 1):
        #  for grid (level i):
        #  all the outer circle (one coord 0 or 4), depends on the grid (level i - 1)
        #  all the inner circle (one coord 1 or 3), depends on the grid (level i + 1)
        


def main():
    all_grids = {}
    update_all_grids(all_grids, 200, 200)
    exit()
    
    minutes = 200
    all_grids = {}
    #  create an empty directory
    for i in range(2 * minutes + 1):
        all_grids[i] = [ [0 for j in range(5)] for k in range(5)]
    print(len(all_grids))
    #  set the input directory
    input_grid = read_input('eg_input.txt')
    all_grids[200] = input_grid
    visual_grid(all_grids[200])
    visual_grid(all_grids[400])

    #  Do the iteration
    #  for minute = k, only change from all_grids[200-k] to all_grids[200+k]
    prev_grids = all_grids
    for m in range(1, minutes+1):
        new_grids = update_all_grids(prev_grids)
        prev_girds = new_grids

    #  sum up all bugs
    total_bug = 0
    for i in range(2 * minutes + 1):
       total_bug += sum_grid(prev_grids[i])
    print("Total number of bugs is %d"%total_bug)


if __name__ == "__main__":
    main()
