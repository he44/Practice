def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    instructions = open(in_fname).read().strip().split('\n')
    coord = [0, 0]
    wpt = [10, 1]
    dir_idx = 0
    direction = DIRS[DIR_NAMES[dir_idx]]
    for instruction in instructions:
        op = instruction[:1]
        arg = int(instruction[1:])
        # moving way point
        if op in DIRS:
            wpt[0] += DIRS[op][0] * arg
            wpt[1] += DIRS[op][1] * arg
        elif op == 'F':
            move0 = arg * wpt[0]
            move1 = arg * wpt[1]
            coord[0] += move0
            coord[1] += move1
        elif op == 'R':
            # [10, 4] became [4, -10]
            # wpt[0] always points to east, wpt[1] always points to north
            offset = arg // 90
            wpt = cl_rotate(wpt, offset)
        elif op == 'L':
            offset = arg // 90
            wpt = cl_rotate(wpt, ( 4 - offset) % 4)

        print("After {}, ship at {}, waypoint at {}".format(instruction, coord, wpt))
    print("Final position at {}, MD is {}".format(coord, abs(coord[0]) + abs(coord[1])))



def cl_rotate(wpt, times):
    # if times is odd, we have to switch wpt[0] and wpt[1]
    # otherwise, only the sign of the values change
    if times % 2 == 0:
        sign0 = sum(DIRS[DIR_NAMES[( 0 + times) % 4]])
        sign1 = sum(DIRS[DIR_NAMES[( 3 + times) % 4]])
        new_wpt = [wpt[0] * sign0, wpt[1] * sign1]
        return new_wpt
    # we have to switch
    else:
        sign0 = sum(DIRS[DIR_NAMES[( 0 + times) % 4]])
        sign1 = sum(DIRS[DIR_NAMES[( 3 + times) % 4]])
        new_wpt = [wpt[1] * sign1, wpt[0] * sign0]
        return new_wpt



DIR_NAMES = ["E", "S", "W", "N"]
DIRS = {
    "E": [1, 0], # E
    "S": [0, -1], # S
    "W": [-1, 0], # W
    "N": [0, 1]
}

if __name__ == "__main__":
    main()

