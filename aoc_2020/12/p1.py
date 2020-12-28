def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    instructions = open(in_fname).read().strip().split('\n')
    coord = [0, 0]
    dir_idx = 0
    direction = DIRS[DIR_NAMES[dir_idx]]
    for instruction in instructions:
        op = instruction[:1]
        arg = int(instruction[1:])
        # only changing position
        if op in DIRS:
            coord[0] += arg * DIRS[op][0]
            coord[1] += arg * DIRS[op][1]
        elif op == 'F':
            coord[0] += arg * direction[0]
            coord[1] += arg * direction[1]
        elif op == 'R':
            offset = arg // 90
            dir_idx = (dir_idx + offset) % 4
            direction = DIRS[DIR_NAMES[dir_idx]]
        elif op == 'L':
            offset = arg // 90
            dir_idx = (dir_idx + (4 - offset)) % 4
            direction = DIRS[DIR_NAMES[dir_idx]]
        print("After {}, at {}".format(instruction, coord))
    print("Final position at {}, MD is {}".format(coord, abs(coord[0]) + abs(coord[1])))



DIR_NAMES = ["E", "S", "W", "N"]
DIRS = {
    "E": [1, 0], # E
    "S": [0, -1], # S
    "W": [-1, 0], # W
    "N": [0, 1]
}

if __name__ == "__main__":
    main()

