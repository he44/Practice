def main():
    in_fname = "i1_eg_3.txt"
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    timestamp = int(lines[0])
    buses = lines[1].strip().split(',')
    buses = [int(x) for x in buses if x != "x"]
    bus_offset = {b:-1 for b in buses}
    raw_info = lines[1].split(',')
    for i in range(len(raw_info)):
        if raw_info[i] != 'x':
            bus_offset[int(raw_info[i])] = i
    print(buses)
    print(bus_offset)

    # we can optimize how many "numbers" to skip
    first = buses[0]
    first_mul = 1
    first_mul = 100000000000000 // first
    while True:
        next_mul = []
        cnum = first * first_mul
        flag = True
        for bus in buses[1:]:
            t = cnum + bus_offset[bus]
            if t % bus != 0:
                flag = False
                guess = ((1 + t // bus) * bus) // first
                next_mul.append(guess)
                break
        if flag:
            break
        first_mul = max(max(next_mul), first_mul + 1)
        print("Tested {}".format(cnum))
    print("First such time stamps is {}".format(cnum))



if __name__ == "__main__":
    main()
