def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"

    passes = open(in_fname).read().strip().split('\n')

    # part 1
    ids = set()
    max_id = float('-inf')
    min_id = float('inf')
    for bpass in passes:
        this_id = get_id(bpass)
        max_id = max(max_id, this_id)
        min_id = min(min_id, this_id)
        ids.add(this_id)

    print("Max id is {}".format(max_id))

    # part 2
    for one_id in range(min_id, max_id + 1):
        if one_id not in ids:
            print("This id might be {}".format(one_id))


def get_id(bpass):
    rmin, rmax = (0, 128)
    cmin, cmax = (0, 8)
    for char in bpass:
        rmid = rmin + (rmax - rmin) // 2
        cmid = cmin + (cmax - cmin) // 2
        if char == "F":
            rmax = rmid
        elif char == "B":
            rmin = rmid
        elif char == "L":
            cmax = cmid
        elif char == "R":
            cmin = cmid
        else:
            print("Something wrong")
            break
    return rmin * 8 + cmin


if __name__ == "__main__":
    main()
