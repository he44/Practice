def main():
    in_file = "i1_eg.txt"
    in_file = "i1.txt"
    lines = open(in_file).read().strip().split('\n')
    black_list = set()
    for line in lines:
        coord = find_tile(line)
        post_process_coord = tuple(coord[0].to_number() + coord[1].to_number())
        # print("Tile {}".format(post_process_coord))
        if post_process_coord not in black_list:
            black_list.add(post_process_coord)
        else:
            black_list.remove(post_process_coord)


    print("Initially we have {} black tiles".format(len(black_list)))


    num_days = 100
    for di in range(num_days):
        # number of black tile neighbors
        ncount = dict()

        # count neighbor of black tiles
        for item in black_list:
            ncount[item] = 0
            x1, x2, y1, y2 = item
            this_coord = [unit(x1,x2), unit(y1,y2)]
            for direction in dirs:
                update = dirs[direction]
                # coordinates of the neighbor
                ncoord = []
                for k in range(2):
                    ncoord.append(this_coord[k] + update[k])
                nlabel = tuple(ncoord[0].to_number() + ncoord[1].to_number())
                if nlabel in black_list:
                    ncount[item] += 1

        # count neighbor for tiles adjacent to black tiles
        # don't recount black ones
        for item in black_list:
            x1, x2, y1, y2 = item
            this_coord = [unit(x1,x2), unit(y1,y2)]
            for direction in dirs:
                update = dirs[direction]
                # coordinates of the neighbor
                ncoord = []
                for k in range(2):
                    ncoord.append(this_coord[k] + update[k])
                nlabel = tuple(ncoord[0].to_number() + ncoord[1].to_number())
                if nlabel in black_list:
                    continue
                if nlabel in ncount:
                    ncount[nlabel] += 1
                else:
                    ncount[nlabel] = 1

        # to_remove
        to_remove = set()
        for item in black_list:
            if ncount[item] == 0 or ncount[item] > 2:
                to_remove.add(item)

        # to_add
        to_add = set()
        for item in ncount:
            if item not in black_list and ncount[item] == 2:
                to_add.add(item)

        for item in to_remove:
            black_list.remove(item)
        for item in to_add:
            black_list.add(item)

        if (di + 1) <= 10 or (di + 1) % 10 == 0:
            print("Day {}: {}".format(di+1, len(black_list)))



# after drawing the diagram, it turns out ne and nw are not opposite
# maybe we should keep using a two part system, one denoting integer
# another denoting sqrt(3)
# so we avoid dealing with floating point number

class unit():
    def __init__(self, one, sq3):
        self.one = one
        self.sq3 = sq3

    def __iadd__(self, other):
        self.one += other.one
        self.sq3 += other.sq3
        return self

    def __add__(self, other):
        ans = unit(self.one + other.one, self.sq3 + other.sq3)
        return ans

    def __str__(self):
        return "{} + {} * sqrt(3)".format(self.one, self.sq3)

    def __repr(self):
        return "unit({},{})".format(self.one, self.sq3)

    def to_number(self):
        return [self.one, self.sq3]

dirs = {
    "e": (unit(2,0), unit(0,0)),
    "w": (unit(-2,0), unit(0,0)),
    "se": (unit(1,0), unit(0, -1)),
    "nw": (unit(-1,0), unit(0, 1)),
    "ne": (unit(1,0), unit(0,1)),
    "sw": (unit(-1,0), unit(0,-1))
}

def find_tile(line):
    # print("Wokring on {}".format(line))
    # e, se, sw, w, nw, ne
    coord = [unit(0,0), unit(0,0)]
    i = 0
    while i < len(line):
        char = line[i]
        # print("Index {} with character {}".format(i, char))
        if char == "s" or char == "n":
            direction = line[i:i+2]
            i += 1
        else:
            direction = line[i]
        i += 1
        update = dirs[direction]
        # update direction
        for k in range(2):
            coord[k] += update[k]
    return tuple(coord)


if __name__ == "__main__":
    main()
