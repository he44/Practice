def main():
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    numbers = [int(x) for x in lines]
    print(numbers)

    def twoPtr(nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                return (nums[lo], nums[hi])
            elif nums[lo] + nums[hi] < target:
                lo += 1
            else:
                hi -= 1
        return None


    numbers.sort()
    # part 2 3-sum
    target = 2020
    for num in numbers:
        res = twoPtr(numbers, target - num)
        if res:
            a1, a2 = res
            print(num, a1, a2, num * a1 * a2)



if __name__ == "__main__":
    main()
