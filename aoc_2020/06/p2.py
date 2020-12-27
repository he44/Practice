def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    groups = open(in_fname).read().strip().split('\n\n')
    ans = 0
    for group in groups:
        ga = compute(group)
        ans += ga
    print(ans)


def compute(group):
    flag = False
    people = group.split('\n')
    for person in people:
        if not flag:
            yesed = set(list(person))
            flag = True
        else:
            yesed &= set(list(person))
    return len(yesed)

if __name__ == "__main__":
    main()
