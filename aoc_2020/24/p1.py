def main():
    in_file = "i1_eg.txt"
    in_file = "i1.txt"
    lines = open(in_file).read().strip().split('\n')
    black_list = set()
    line = "nwwswee"
    coord = find_tile(line)
    for line in lines:
        coord = find_tile(line)
        post_process_coord = tuple(coord[0].to_number() + coord[1].to_number())
        print("Tile {}".format(post_process_coord))
        if post_process_coord not in black_list:
            black_list.add(post_process_coord)
        else:
            black_list.remove(post_process_coord)
    # print(black_list)
    print("Number of tiles remanining black afterwards", len(black_list))


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
    print("Wokring on {}".format(line))
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
