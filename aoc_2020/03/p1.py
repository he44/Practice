def main():
    in_fname = "i1.txt"
    in_fname = "i1_eg.txt"
    lines = open(in_fname).read().strip().split('\n')
    h = len(lines)
    pattern = [[] for _ in range(h)]
    for line in lines:
        for char in line:
            if char == "#":
                pass




if __name__ == "__main__":
    main()
