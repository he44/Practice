input_name = "in_14_eg.txt"
input_name = "in_14.txt"

with open(input_name, "r") as fp:
    lines = fp.readlines()

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
    bin_val = format(int(val), "#038b")[2:]
    assert len(bin_val) == 36, "wrong length {}".format(len(bin_val))

    masked_bin_val = [bin_val[i] if raw_mask[i] == 'X' else raw_mask[i] for i in range(36)]
    masked_bin_val = ''.join(masked_bin_val)

    write_val = int(masked_bin_val, base=2)
    print(raw_mask)
    print(bin_val)
    print(masked_bin_val)
    
    if addr in memory:
        ans -= memory[addr]
    memory[addr] = write_val
    ans += write_val

print("Part 1, sum is {}".format(ans))

