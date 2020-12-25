def main():
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    numbers = [int(x) for x in lines]
    print(numbers)

    # part 1 two sum
    target = 2020
    opposite = set()
    for num in numbers:
        opposite.add(target - num)

    for num in numbers:
        if num in opposite:
            print(num, target - num, num * (target - num))


if __name__ == "__main__":
    main()
