def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    groups = open(in_fname).read().strip().split('\n\n')
    ans = 0
    for group in groups:
        ans += compute(group)
    print(ans)


def compute(group):
    yesed = set()
    people = group.split('\n')
    for person in people:
        yesed |= set(list(person))
    return len(yesed)

if __name__ == "__main__":
    main()
