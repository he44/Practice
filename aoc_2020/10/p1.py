def main():
    in_fname = "i1_eg_2.txt"
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    output_joltages = [int(x) for x in lines]
    device_out = max(output_joltages) + 3

    # if we are using all adapters, I can just sort and compute
    chains = sorted(output_joltages)
    cur = 0
    diff_1 = 0
    diff_3 = 0
    for output_j in chains + [device_out]:
        diff = abs(output_j - cur)
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        cur = output_j
    print(diff_1, diff_3, diff_1 * diff_3)


if __name__ == "__main__":
    main()
