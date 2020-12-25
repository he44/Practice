def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    ans = 0
    for line in lines:
        if check_policy(line):
            ans += 1
    print(ans)


def check_policy(line):
    policy, passwd = line.strip().split(": ")
    times, char = policy.split(" ")
    idx1, idx2 = times.split('-')
    idx1 = int(idx1)
    idx2 = int(idx2)
    return ((passwd[idx1-1] == char) ^ (passwd[idx2-1] == char))


if __name__ == "__main__":
    main()
