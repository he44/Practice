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

    target = nums[ni]
    print("Target is {}".format(target))

    # Let's build a O(n^2) table that contains all the contiguous set sum?
    # we don't need to fill the whole thing because if it gets too large
    # we simply stop
    # also, all numbers seem to be positive
    # t[i][j] is the sum of nums[i, j]
    # i goes from 0 to n-1, 
    # j goes from i + 2 to n - 1
    


    n = len(nums)

    table = [[-1 for j in range(n + 1)] for i in range(n)]

    for i in range(n):
        for j in range(i + 1):
            table[i][j] = 0

    for i in range(n-1):
        table[i][i + 1] = nums[i]
        table[i][i + 2] = nums[i] + nums[i + 1]

    # fill in 
    ans = None
    found = False
    for i in range(n-1):
        for j in range(i + 2, n + 1):
            if not found:
                table[i][j] = table[i][j-1] + nums[j-1]
                if table[i][j] == target:
                    found = True
                    ans = (i, j)
                    break
                if table[i][j] > target:
                    break
    
    lo, hi = ans
    weakness = min(nums[lo:hi]) + max(nums[lo:hi])
    print(weakness)






if __name__ == "__main__":
    main()
