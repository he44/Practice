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

def sum_all(grids):
    total = 0
    for i in grids:
        total += sum_grid(grids[i])
    return total


#  Update all grids
#  prev_grids: a dictionary of all the possible grids
def update_all_grids(prev_grids, minutes, current_minute):
    updated_grids = prev_grids
    #  for current_minute, only 2 * current_minute + 1 grids need to be udpated
    for i in range(minutes - current_minute, minutes + current_minute + 1):
        #  basic counting
        counts = [[0 for x in range(5)] for y in range(5)]
        for r in range(5):
            for c in range(5):
                counts[r][c] = count_in_adjacent_tiles(prev_grids[i], r, c)
        #  all the outer circle (one coord 0 or 4), depends on the grid (level i - 1)
        if i - 1 >= minutes - current_minute:
            for c in range(5):
                counts[0][c] += prev_grids[i-1][1][2]
                counts[4][c] += prev_grids[i-1][3][2]
            for r in range(5):
                counts[r][0] += prev_grids[i-1][2][1]
                counts[r][4] += prev_grids[i-1][2][3]
        #  4 cells depend on the grid (level i + 1), in the problem notation, 8,12,14,18
        if i + 1 < minutes + current_minute + 1:
            counts[1][2] += sum_row(prev_grids[i+1], 0)
            counts[2][1] += sum_col(prev_grids[i+1], 0)
            counts[3][2] += sum_row(prev_grids[i+1], 4)
            counts[2][3] += sum_col(prev_grids[i+1], 4)
        #  update
        for r in range(5):
            for c in range(5):
                if prev_grids[i][r][c] == 1 and counts[r][c] != 1:
                    updated_grids[i][r][c] = 0
                #  An empty space becomes infested with a bug
                #  if exactly one or two bugs are adjacent to it.
                elif prev_grids[i][r][c] == 0 and counts[r][c] in (1,2):
                    updated_grids[i][r][c] = 1
                else:
                    updated_grids[i][r][c] = prev_grids[i][r][c]
        updated_grids[i][2][2] = 0
        


def main():
    """
    minutes = 200
    all_grids = {}
    for i in range(2 * minutes + 1):
        all_grids[i] = [ [0 for j in range(5)] for k in range(5)]
    update_all_grids(all_grids, 200, 200)
    exit()
    """
    
    minutes = 10
    all_grids = {}
    #  create an empty directory
    for i in range(2 * minutes + 1):
        all_grids[i] = [ [0 for j in range(5)] for k in range(5)]
    print(len(all_grids))
    #  set the input directory
    input_grid = read_input('eg_input.txt')
    all_grids[minutes] = input_grid
    print("Initially, there are %d bugs"%sum_all(all_grids))

    #  Do the iteration
    #  for minute = k, only change from all_grids[200-k] to all_grids[200+k]
    prev_grids = all_grids
    for m in range(1, minutes+1):
        new_grids = update_all_grids(prev_grids, minutes, m)
        prev_girds = new_grids
        m_sum = sum_all(prev_grids)
        print("After %d minutes, total number of bugs is %d"%(m, m_sum))

    #  sum up all bugs
    total_bug = sum_all(prev_grids)
    print("Total number of bugs is %d"%total_bug)

    print(len(prev_grids))
    exit()
    #  visualizing
    for i in prev_grids:
        visual_grid(prev_grids[i])


if __name__ == "__main__":
    main()
