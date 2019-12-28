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
input_file = 'eg_input.txt'
minutes = 1
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
        print(counts[level])
        #  add the counts from level - 1 (the level that contains this one)
        #  outer gets affected
        # @something
        #  add the counts from level + 1 (the level that's within this one)
        #  only four cells get affected
        # @something
    #  Phase 2: updating all based on counts
    for level in range(-cur_m, cur_m + 1):
        for r in range(const_dim):
            for c in range(const_dim):
                levels[level].update(counts[level])
        
        


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
