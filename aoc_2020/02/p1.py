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
    min_t, max_t = times.split('-')
    min_t = int(min_t)
    max_t = int(max_t)
    return (min_t <= passwd.count(char) <= max_t)


if __name__ == "__main__":
    main()
