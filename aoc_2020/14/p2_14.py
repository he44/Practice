input_name = "p2_in_14_eg.txt"
input_name = "in_14.txt"

LEN = 36

with open(input_name, "r") as fp:
    lines = fp.readlines()


from collections import Counter
def floating_addr(masked_addr):
    possible_addrs = set()
    num_x = masked_addr.count('X')
    num_choices = 2 ** num_x
    # each bit in num_x encodes a choice
    for i in range(num_choices):
        choice = format(i, "#0{}b".format(num_x + 2))[2:]
        print(choice)
        # replace this choice
        one_addr = list(masked_addr)
        count = 0
        for j in range(LEN):
            if one_addr[j] == "X":
                one_addr[j] = choice[count]
                count += 1
        one_addr = ''.join(one_addr)
        one_addr_in_int = int(one_addr, base=2)
        if one_addr_in_int not in possible_addrs:
            possible_addrs.add(one_addr_in_int)
    return possible_addrs


ans = 0
memory = dict()
for line in lines:
    # update mask
    if line.find('mask') != -1:
        _, raw_mask = line.strip().split(' = ')
        continue
    # write to memory
    addr, val = line.strip().split(' = ')
    addr_str = addr.split('[')[1]
    addr_str = addr_str.split(']')[0]
    addr = int(addr_str)

    # apply mask on the value
    val = int(val)
    addr_bin = format(addr, "#038b")[2:]

    masked_bin_addr = [raw_mask[i] if raw_mask[i] != '0' else addr_bin[i] for i in range(36)]
    masked_bin_addr = ''.join(masked_bin_addr)
    # print("mask: ", raw_mask)
    # print("addr: ", addr_bin)
    # print("addr m", masked_bin_addr)
    # print("possible addrs: ")
    # for pa in floating_addr(masked_bin_addr):
        # print(pa)

    possible_addrs = floating_addr(masked_bin_addr)
    for pa in possible_addrs:
        if pa in memory:
            ans -= memory[pa]
        memory[pa] = val
        ans += val

print("Part 2, sum is {}".format(ans))

