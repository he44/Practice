import copy

const_dim = 5

class Grid:
    def __init__(self, file_name='eg_input.txt', val=None):
        if val != None:
            self.grid = [[val for r in range(const_dim)] for c in range(const_dim)]
        else:
            self.grid = [[val for r in range(const_dim)] for c in range(const_dim)]
            with open(file_name, 'r') as f_csv:
                lines = f_csv.readlines()
                for r in range(const_dim):
                    line = lines[r].strip()
                    for c in range(const_dim):
                        if line[c] == '#':
                            self.grid[r][c] = 1
                        else:
                            self.grid[r][c] = 0

    def __repr__(self):
        string = ''
        for row in self.grid:
            string += str(row) + '\n'
        return string[:-1]

    def set_val(self, r, c, val):
        self.grid[r][c] = val

    def get_val(self, r, c):
        return self.grid[r][c]

    def get_grid(self):
        return self.grid

    def sum_all(self):
        total = 0
        for row in self.grid:
            total += sum(row)
        return total

    def sum_row(self, r):
        total = 0
        return sum(self.grid[r])

    def sum_col(self, c):
        total = 0
        for r in range(const_dim):
            total += self.grid[r][c]
        return total

    def update(self, counts):
        for r in range(const_dim):
            for c in range(const_dim):
                if self.grid[r][c] == 1 and counts[r][c] != 1:
                    self.grid[r][c] = 0
                elif self.grid[r][c] == 0 and counts[r][c] in (1,2):
                    self.grid[r][c] = 1

    def count_within(self):
        count = [[0 for x in range(const_dim)] for y in range(const_dim)]
        for r in range(const_dim):
            for c in range(const_dim):
                #  top neighbor
                if r - 1 >= 0:
                    count[r][c] += int(self.grid[r-1][c] == 1)
                #  left neighbor
                if c - 1 >= 0:
                    count[r][c] += int(self.grid[r][c-1] == 1)
                #  bottom neighbor
                if r + 1 < const_dim:
                    count[r][c] += int(self.grid[r+1][c] == 1)
                #  right neighbor
                if c + 1 < const_dim:
                    count[r][c] += int(self.grid[r][c+1] == 1)
        return count
        
        

"""
Initializaton:
1.) there should be at most 2 * minutes + 1 levels that get activated
2.) level 0: the input file
"""
input_file = '24_input.txt'
minutes = 200
levels = {}
for key in range(-minutes, minutes+1):
    levels[key]  = Grid(val=0)
levels[0] = Grid(input_file)

"""
Updating
"""
for cur_m in range(1, minutes+1):
    #  Refershing counts for this iteration
    counts = {}
    for key in range(-cur_m, cur_m + 1):
        counts[key] = Grid(val=0)
    #  Phase 1: collecting all the counts
    for level in range(-cur_m, cur_m + 1):
        #  updating counts[pos_lev]
        #  basic counts (within each level)
        counts[level] = levels[level].count_within()
        #print(counts[level])
        #  add the counts from level - 1 (the level that contains this one)
        #  outer gets affected
        if level - 1 >= -cur_m:
            for r in range(const_dim):
                counts[level][r][0] += levels[level-1].get_val(2, 1)
                counts[level][r][4] += levels[level-1].get_val(2, 3)
            for c in range(const_dim):
                counts[level][0][c] += levels[level-1].get_val(1, 2)
                counts[level][4][c] += levels[level-1].get_val(3, 2)
        #  add the counts from level + 1 (the level that's within this one)
        #  only four cells get affected
        if level + 1 < cur_m + 1:
            counts[level][1][2] += levels[level+1].sum_row(0)
            counts[level][3][2] += levels[level+1].sum_row(4)
            counts[level][2][1] += levels[level+1].sum_col(0)
            counts[level][2][3] += levels[level+1].sum_col(4)
            #counts[level][1][2] += levels[level+1]
        """
        if cur_m == 2 and level == 2:
            print(levels[level-1])
            print("counts for level %d"%level)
            print(counts[level])
        """
    #  Phase 2: updating all based on counts
    for level in range(-cur_m, cur_m + 1):
        for r in range(const_dim):
            for c in range(const_dim):
                levels[level].update(counts[level])
        levels[level].set_val(2,2,0)
        
        


"""
Count how many bugs we have in total
"""
all_bug = 0
for key in range(-minutes, minutes+1):
    bug_count = levels[key].sum_all()
    all_bug += bug_count
    print('level %d'%key)
    print(levels[key])
    print(bug_count)
    print('')
print('After %d mintues, having %d bugs'%(minutes, all_bug))
