def main():
    in_fname = "i1_eg.txt"; pre_len = 5;
    in_fname = "i1.txt"; pre_len = 25;
    lines = open(in_fname).read().strip().split('\n')
    nums = [int(x) for x in lines]
    for ni in range(pre_len, len(nums)):
        preamble = nums[ni - pre_len:ni]
        s_preamble = sorted(preamble)
        min_sum = s_preamble[0] + s_preamble[1]
        max_sum = s_preamble[-1] + s_preamble[-2]
        if not (min_sum <= nums[ni] <= max_sum):
            break
    print("The first number that fails is {}".format(nums[ni]))


if __name__ == "__main__":
    main()
