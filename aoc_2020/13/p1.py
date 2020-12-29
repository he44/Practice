def main():
    in_fname = "i1.txt"
    in_fname = "i1_eg.txt"
    lines = open(in_fname).read().strip().split('\n')
    timestamp = int(lines[0])
    buses = lines[1].strip().split(',')
    buses = [int(x) for x in buses if x != "x"]
    print(timestamp)
    print(buses)
    # diff
    min_wait = max(buses) 
    bus_id = -1
    for bus in buses:
        this_arrive = ( 1 + timestamp // bus) * bus 
        this_wait = this_arrive - timestamp
        print("Bus {} arrives at {}, waiting {}".format(bus, this_arrive, this_wait))
        if this_wait < min_wait:
            min_wait = this_wait
            bus_id = bus
    print("Bus {}, Wait {}, Ans {}".format(bus_id, min_wait, bus_id * min_wait))




if __name__ == "__main__":
    main()
