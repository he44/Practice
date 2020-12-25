def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    h = len(lines)
    pattern = [[] for _ in range(h)]
    for i in range(h):
        line = lines[i]
        for char in line.strip():
            if char == "#":
                pattern[i].append(1)
            else:
                pattern[i].append(0)
    print(pattern)
    w = len(pattern[0])

    def check(pattern, sy, sx):
        cur = (0,0)
        cx, cy = cur
        ans = 0
        while cx < h:
            # print(cx, cy)
            ans += pattern[cx][cy]
            cx += sx
            cy  = (cy + sy) % w
        return ans
    
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]
    
    ans = 1
    for sx, sy in slopes:
        nt = check(pattern, sx, sy)
        print(nt)
        ans *= nt

    print("Product is {}".format(ans))





if __name__ == "__main__":
    main()
