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

    # arrangements
    LENGTH = round(math.sqrt(len(all_grids)))
    arrange = [[0 for _ in range(LENGTH)] for _ in range(LENGTH)]
    arrange[0][0] = tl_id
    placed = set()
    placed.add(tl_id)

    for r in range(LENGTH):
        for c in range(LENGTH):
            if arrange[r][c] != 0:
                continue
            # build on previous one
            if r == 0 or c == 0:
            # we also need to handle orientation

            # if on borader, easier, cause we can specify that "1"

            # we need to use this one cid
            cid.rotate(dst_id, pb_key)





BOARDERS = [
    "top", "right", "bottom", "left"
]

class Grid():
    def __init__(self, index, grid):
        self.idx = index
        self.grid = grid
        # let's get boraders as top, right, bottom and left
        self.boarders = {
            "top": self.grid[0],
            "right": ''.join([x[-1] for x in self.grid]),
            "bottom": self.grid[-1],
            "left": ''.join([x[0] for x in self.grid])
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

    # rotate or flip the grid such that 
    def rotate(self, side, key):
        pass

    def flip(self):
        pass



if __name__ == "__main__":
    main()
