import math
def main():
    in_fname = "i1.txt"
    in_fname = "i1_eg.txt"

    tiles = open(in_fname).read().strip().split('\n\n')

    #
    # store all tiles in an object
    # 
    all_grids = {}
    for tile in tiles:
        rows = tile.split('\n')
        idx = int(rows[0].split(' ')[1][:-1])

        grid = rows[1:]

        this_grid = Grid(idx, rows[1:])
        all_grids[idx] = this_grid


    print("Number of grids is {}".format(len(all_grids)))

    # 
    # Count appearances of each boarder
    #
    boarder_counts = {}
    for gid in all_grids:
        tile = all_grids[gid]
        for bid in BOARDERS:
            key = tile.boarder_to_key(bid)
            if key not in boarder_counts:
                boarder_counts[key] = [gid]
            else:
                boarder_counts[key].append(gid)

    print("Number of unique boarders is {}".format(len(boarder_counts)))

    #
    # Pick the four courner pieces
    #
    corner_ids = []
    for gid in all_grids:
        times = 0
        tile = all_grids[gid]
        for bid in BOARDERS:
            times += len(boarder_counts[tile.boarder_to_key(bid)])
        if times == 6:
            corner_ids.append(gid)

    # Let's pick the top first corner correct so it's easier to compare answer
    tl_id = corner_ids[0]
    print("Picking Tile {} as top left".format(tl_id))
    print("Corner IDs: {}".format(corner_ids))

    for item in boarder_counts:
        print(boarder_counts[item])


    print(all_grids[1951].all_boarders())
    print(all_grids[2729].all_boarders())

    # arrangements
    LENGTH = round(math.sqrt(len(all_grids)))
    arrange = [[0 for _ in range(LENGTH)] for _ in range(LENGTH)]
    arrange[0][0] = tl_id
    placed = set()
    not_placed = set([x for x in all_grids])
    placed.add(tl_id)
    not_placed.remove(tl_id)

    print("Before rotating/flipping the top left corner")
    print(all_grids[tl_id])
    print("counts")
    for dirs in BOARDERS:
        print(dirs, boarder_counts[all_grids[tl_id].boarder_to_key(dirs)])
    
    # we must rotate top left such that its left and top occured only once
    for i in range(4):
        top = all_grids[tl_id].boarder_to_key('top')
        left = all_grids[tl_id].boarder_to_key('left')
        if len(boarder_counts[top]) == 1 and len(boarder_counts[left]) == 1:
            break
        all_grids[tl_id].rotate_cl()

    top = all_grids[tl_id].boarder_to_key('top')
    left = all_grids[tl_id].boarder_to_key('left')
    if len(boarder_counts[top]) != 1 or len(boarder_counts[left]) != 1:
        all_grids[tl_id].flip_lr()
        for i in range(4):
            top = all_grids[tl_id].boarder_to_key('top')
            left = all_grids[tl_id].boarder_to_key('left')
            if boarder_counts[top] == 1 and boarder_counts[left] == 1:
                break
            all_grids[tl_id].rotate_cl()
    
    print("After rotating/flipping the top left corner")
    print(all_grids[tl_id])
    print("counts")
    for dirs in BOARDERS:
        print(dirs, boarder_counts[all_grids[tl_id].boarder_to_key(dirs)])

    print(not_placed)

    print(arrange)

    for r in range(LENGTH):
        for c in range(LENGTH):
            print("Working on r = {}, c = {}".format(r,c))
            if arrange[r][c] != 0:
                continue
            # need to check the left piece
            try:
                if c >= 1:
                    ln = arrange[r][c-1]
                    print("  Left neighbor is {}".format(ln))
                    target_lb = all_grids[ln].boarder_to_key('right')
                    lb_brd = all_grids[ln].boarder('right')
                else:
                    target_lb = None

                # need to check the right piece
                if r >= 1:
                    tn = arrange[r-1][c]
                    print("  Top neighbor is {}".format(tn))
                    target_tb = all_grids[tn].boarder_to_key('bottom')
                    tb_brd = all_grids[ln].boarder('bottom')
                    tb_brd = ''.join([x for x in reversed(tb_brd)])
                else:
                    target_tb = None

                print("Trying to match left {}, top {}".format(target_lb, target_tb))

                # try which block it is
                reqs = []
                if target_lb and target_tb:
                    for tid in not_placed:
                        tile = all_grids[tid]
                        tid_has = tile.all_boarders()
                        if target_lb in tid_has and target_tb in tid_has:
                            arrange[r][c] = tid
                            break
                    placed.add(tid)
                    not_placed.remove(tid)
                    reqs.append(("top", tb_brd))
                    reqs.append(("left", lb_brd))
                elif target_lb:
                    for tid in not_placed:
                        tile = all_grids[tid]
                        tid_has = tile.all_boarders()
                        if target_lb in tid_has:
                            arrange[r][c] = tid
                            break
                    placed.add(tid)
                    not_placed.remove(tid)
                    reqs.append(("left", lb_brd))
                elif target_tb:
                    for tid in not_placed:
                        tile = all_grids[tid]
                        tid_has = tile.all_boarders()
                        print(" ----- Tried {}".format(tid))
                        print(tile.all_boarders())
                        if target_tb in tid_has:
                            arrange[r][c] = tid
                            break
                    placed.add(tid)
                    not_placed.remove(tid)
                    reqs.append(("top", tb_brd))
            except:
                print("Not working")
            print("Before transform")
            print(all_grids[1951])
            print(all_grids[2311])
            print(all_grids[3079])
            print(all_grids[2729])

            all_grids[tid].transform_till_match(reqs)
            print("After transform")
            print(all_grids[tid])
            print(arrange)

    print(arrange)


    # "
    # Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters.
    # "

    # so at collaging it's okay to go whatever way
    # but after collaging, only one position is guaranteed to find sea monsters?



BOARDERS = ["top", "right", "bottom", "left"]


class Grid():
    def __init__(self, index, grid):
        self.idx = index
        self.grid = grid
        self.size = len(grid)
        # let's get boraders as top, right, bottom and left
        # all of them in clockwise ordering, which helps make rotation easier
        self.boarders = {
            "top": self.grid[0], # left to right
            "right": ''.join([x[-1] for x in self.grid]), # top to bottom
            "bottom": ''.join([x for x in reversed(self.grid[-1])]), # right to left
            "left": ''.join([x[0] for x in reversed(self.grid)]) # bottom to top
        }

    def show_boarder(self):
        print("Tile {}".format(self.idx))
        for item in self.boarders:
            print("{} boarder is {}".format(item, self.boarders[item]))
    
    def boarder_to_key(self, bid):
        boarder = self.boarders[bid]
        possibles = [boarder, ''.join(reversed(boarder))]
        possibles.sort()
        key = tuple(possibles)
        return key

    def boarder(self, bid):
        return self.boarders[bid]

    def all_boarders(self):
        key_set = set()
        for dirs in BOARDERS:
            key_set.add(self.boarder_to_key(dirs))
        return key_set

    # rotate or flip the grid such that 
    def rotate_cl(self):
        # change the grid
        new_grid = ['' for _ in range(self.size)]
        for c in range(self.size):
            col = ''.join([x[c] for x in reversed(self.grid)])
            new_grid[c] = col
        self.grid = new_grid
        # change the boarder
        self.boarders = {
            "top": self.grid[0], # left to right
            "right": ''.join([x[-1] for x in self.grid]), # top to bottom
            "bottom": ''.join([x for x in reversed(self.grid[-1])]), # right to left
            "left": ''.join([x[0] for x in reversed(self.grid)]) # bottom to top
        }

    def flip_lr(self):
        # change the grid
        new_grid = ['' for _ in range(self.size)]
        for r in range(self.size):
            new_grid[r] = ''.join(reversed(self.grid[r]))
        self.grid = new_grid
        # change the boarder
        self.boarders = {
            "top": self.grid[0], # left to right
            "right": ''.join([x[-1] for x in self.grid]), # top to bottom
            "bottom": ''.join([x for x in reversed(self.grid[-1])]), # right to left
            "left": ''.join([x[0] for x in reversed(self.grid)]) # bottom to top
        }

    def satisfy_reqs(self, reqs: list) -> bool:
        for dire, brd in reqs:
            if self.boarder(dire) != brd:
                return False
        return True

    def transform_till_match(self, reqs: list):
        # rotate 4 times
        for i in range(4):
            if self.satisfy_reqs(reqs):
                break
            self.rotate_cl()

        # flip and rotate 4 times
        if self.satisfy_reqs(reqs):
            self.flip_lr()
            for i in range(4):
                if self.satisfy_reqs(reqs):
                    break
                self.rotate_cl()

    def __str__(self):
        out = ""
        for row in self.grid:
            out = out + "{}\n".format(row)
        return out




if __name__ == "__main__":
    main()
