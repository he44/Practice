def main():
    in_fname = "i1.txt"
    in_fname = "i1_eg.txt"

    tiles = open(in_fname).read().strip().split('\n\n')

    # store all tiles in an object
    grids = {}
    for tile in tiles:
        rows = tile.split('\n')
        idx = int(rows[0].split(' ')[1][:-1])

        grid = rows[1:]

        this_grid = Grid(idx, rows[1:])
        grids[idx] = this_grid


    print(len(grids))

    # we need to find tiles with (1,1,2,2) counts for their boarders
    # these are the corners

    # how to handle flipping and rotation?
    # well, there can only be two types of boarders. 
    # the string and its reverse, so we put them together as the key
    # to eunsure consistency we sort (string, rev(string)) as well

    boarders = {}
    for gid in grids:
        tile = grids[gid]
        for bid in BOARDERS:
            key = tile.boarder_to_key(bid)
            if key not in boarders:
                boarders[key] = [gid]
            else:
                boarders[key].append(gid)
    print(len(boarders))


    corner_ids = []
    for gid in grids:
        times = 0
        tile = grids[gid]
        for bid in BOARDERS:
            times += len(boarders[tile.boarder_to_key(bid)])
        if times == 6:
            corner_ids.append(gid)

    print(corner_ids)
    ans = 1
    for gid in corner_ids:
        ans *= gid
    print("Part 1 answer is {}".format(ans))





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


if __name__ == "__main__":
    main()
