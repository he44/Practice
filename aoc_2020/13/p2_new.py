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


    # we need number x that satisifies: x = (bus - bus_offset[bus] % bus) % bus
    # all the buses in this input are prime numbers
    prod = 1
    for bus in buses:
        prod *= bus

    ans = 0
    for bus in buses:
        Mi = prod // bus
        print("Working on mod_inverse({}, {})".format(Mi, bus))
        # ti = mod_inverse(Mi, bus)
        ti = modinv(Mi, bus)
        remainder = (bus - bus_offset[bus] % bus) % bus
        ans += remainder * ti * Mi
        print("finishing {}".format(bus))

    ans %= prod
    print(ans)


# find y s.t (yx) = 1 (mod p) where x and y are integers
# let's implement the naive way for now
def mod_inverse(x, p):
    mul = 1
    while True:
        cnum = mul * p + 1
        if cnum % x == 0:
            break
        mul += 1
    return cnum // x

# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == "__main__":
    main()
