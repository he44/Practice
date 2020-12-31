def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    p1, p2 = open(in_fname).read().strip().split('\n\n')
    p1_raw = p1.split('\n')[1:]
    p1_cards = [int(x) for x in p1_raw]
    print(p1_cards)
    p2_raw = p2.split('\n')[1:]
    p2_cards = [int(x) for x in p2_raw]
    print(p2_cards)
    win_hands = play(p1_cards, p2_cards)
    print(win_hands)

    ans = 0
    mul = 1
    for val in reversed(win_hands):
        ans += val * mul
        mul += 1
    print(ans)


def play(p1_cards, p2_cards):
    while len(p1_cards) > 0 and len(p2_cards) > 0:
        p1_d = p1_cards.pop(0)
        p2_d = p2_cards.pop(0)
        if p1_d > p2_d:
            p1_cards.append(p1_d)
            p1_cards.append(p2_d)
        else:
            p2_cards.append(p2_d)
            p2_cards.append(p1_d)

    if len(p1_cards) == 0:
        return p2_cards
    else:
        return p1_cards


if __name__ == "__main__":
    main()
