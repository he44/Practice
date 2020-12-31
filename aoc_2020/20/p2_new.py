import math
def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"

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

    # test
    # next_id = 2729
    # print(all_grids[next_id])
    # all_grids[next_id].rotate_cl()
    # print(all_grids[next_id])
    # return


    # tl_id = 1951
    # for i in range(4):
        # top_key = all_grids[tl_id].boarder_to_key('top')
        # left_key = all_grids[tl_id].boarder_to_key('left')
        # if len(boarder_counts[top_key]) == 1 and len(boarder_counts[left_key]) == 1:
            # break
        # all_grids[tl_id].rotate_cl()

    # top_key = all_grids[tl_id].boarder_to_key('top')
    # left_key = all_grids[tl_id].boarder_to_key('left')
    # if len(boarder_counts[top_key]) != 1 or len(boarder_counts[left_key]) != 1:
        # all_grids[tl_id].flip_lr()
        # for i in range(4):
            # top_key = all_grids[tl_id].boarder_to_key('top')
            # left_key = all_grids[tl_id].boarder_to_key('left')
            # if len(boarder_counts[top_key]) == 1 and len(boarder_counts[left_key] == 1):
                # break
            # all_grids[tl_id].rotate_cl()

    # print("Setting top left correct")
    # print(all_grids[tl_id])

    # next_id = 2729

    # reqs = []
    # ln = 1951
    # print("  Left neighbor is {}".format(ln))
    # target_lb = all_grids[ln].boarder_to_key('right')
    # lb_brd = all_grids[ln].boarder('right')

    # reqs.append(("left", lb_brd))
    # print(reqs)
    # print(all_grids[next_id].satisfy_reqs(reqs))
    # all_grids[next_id].transform_till_match(reqs)
    # print(all_grids[next_id].satisfy_reqs(reqs))
    # return
    # test done


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


    print("Picking top left")
    print(all_grids[tl_id])
    # put the top left in shape (top and left must have count 1)
    # rotate first
    for i in range(4):
        top_key = all_grids[tl_id].boarder_to_key('top')
        left_key = all_grids[tl_id].boarder_to_key('left')
        if len(boarder_counts[top_key]) == 1 and len(boarder_counts[left_key]) == 1:
            break
        all_grids[tl_id].rotate_cl()

    top_key = all_grids[tl_id].boarder_to_key('top')
    left_key = all_grids[tl_id].boarder_to_key('left')
    if len(boarder_counts[top_key]) != 1 or len(boarder_counts[left_key]) != 1:
        all_grids[tl_id].flip_lr()
        for i in range(4):
            top_key = all_grids[tl_id].boarder_to_key('top')
            left_key = all_grids[tl_id].boarder_to_key('left')
            if len(boarder_counts[top_key]) == 1 and len(boarder_counts[left_key] == 1):
                break
            all_grids[tl_id].rotate_cl()

    print("Setting top left correct")
    print(all_grids[tl_id])

    not_placed = set([x for x in all_grids])
    not_placed.remove(tl_id)

    LENGTH = round(math.sqrt(len(all_grids)))
    arrange = [[0 for _ in range(LENGTH)] for _ in range(LENGTH)]
    arrange[0][0] = tl_id

    # edge tile
    for item in all_grids:
        if all_grids[item].is_edge_tile(boarder_counts):
            print("Tile {} is edge tile".format(item))

    print("Starting point")
    print(arrange)

    for r in range(LENGTH):
        for c in range(LENGTH):
            print("Working on r = {}, c = {}".format(r,c))
            if arrange[r][c] != 0:
                continue
            # need to check the left piece
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
                tb_brd = all_grids[tn].boarder('bottom')
            else:
                target_tb = None

            # try which block it is
            reqs = []
            if target_lb and target_tb:
                for tid in not_placed:
                    tile = all_grids[tid]
                    tid_has = tile.all_boarders()
                    if target_lb in tid_has and target_tb in tid_has:
                        arrange[r][c] = tid
                        break
                not_placed.remove(tid)
                reqs.append(("top", tb_brd))
                reqs.append(("left", lb_brd))
            elif target_lb:
                for tid in not_placed:
                    tile = all_grids[tid]
                    if not tile.is_edge_tile(boarder_counts):
                        continue
                    tid_has = tile.all_boarders()
                    if target_lb in tid_has:
                        arrange[r][c] = tid
                        break
                not_placed.remove(tid)
                reqs.append(("left", lb_brd))
            elif target_tb:
                for tid in not_placed:
                    tile = all_grids[tid]
                    if not tile.is_edge_tile(boarder_counts):
                        continue
                    tid_has = tile.all_boarders()
                    if target_tb in tid_has:
                        arrange[r][c] = tid
                        break
                not_placed.remove(tid)
                reqs.append(("top", tb_brd))

            # transform it to match
            all_grids[tid].transform_till_match(reqs)

            # one placed
            print("Tile {} properly placed at R = {}, C = {}".format(tid, r, c))
            print(" ---------------------------------- ")
            print(all_grids[tid])
            print(" ---------------------------------- ")
    
    print("Collage results are:")
    print(arrange)



BOARDERS = ["top", "right", "bottom", "left"]

class Grid():
    def __init__(self, index, grid):
        self.idx = index
        self.grid = grid
        self.size = len(grid)
        self.boarders = {}
        self._log_boarder()

    def _log_boarder(self):
        self.boarders = {
            "top": self.grid[0], # left to right
            "right": ''.join([x[-1] for x in self.grid]), # top to bottom
            "bottom": self.grid[-1],
            "left": ''.join([x[0] for x in self.grid])
        }

    def show_boarder(self):
        print("Tile {}".format(self.idx))
        for item in self.boarders:
            print("{} boarder is {}".format(item, self.boarders[item]))

    def is_edge_tile(self, boarder_counts) -> bool:
        num = 0
        for bid in self.boarders:
            num += len(boarder_counts[self.boarder_to_key(bid)])
        if num == 7 or num == 6:
            return True
    
    def boarder_to_key(self, bid) -> tuple:
        boarder = self.boarders[bid]
        possibles = [boarder, ''.join(reversed(boarder))]
        possibles.sort()
        key = tuple(possibles)
        return key

    def boarder(self, bid) -> str:
        return self.boarders[bid]

    def all_boarders(self) -> set():
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
        self._log_boarder()

    def flip_lr(self):
        # change the grid
        new_grid = ['' for _ in range(self.size)]
        for r in range(self.size):
            new_grid[r] = ''.join(reversed(self.grid[r]))
        self.grid = new_grid
        # change the boarder
        self._log_boarder()

    def satisfy_reqs(self, reqs: list) -> bool:
        for dire, brd in reqs:
            if self.boarder(dire) != brd:
                return False
        return True

    def transform_till_match(self, reqs: list):
        if self.idx == 2311:
            print("For 2311, reqs are")
            for dire, brd in reqs:
                print(dire, brd)
        # rotate 4 times
        for i in range(4):
            if self.satisfy_reqs(reqs):
                break
            self.rotate_cl()

        # flip and rotate 4 times
        if not self.satisfy_reqs(reqs):
            self.flip_lr()
            for i in range(4):
                if self.satisfy_reqs(reqs):
                    break
                self.rotate_cl()

        assert self.satisfy_reqs(reqs), "Tile {} is not properly placed".format(self.idx)

    def __str__(self):
        out = ""
        for row in self.grid:
            out = out + "{}\n".format(row)
        return out

if __name__ == "__main__":
    main()
