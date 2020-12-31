def main():
    in_fname = "i2_eg.txt"
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    p1, p2 = open(in_fname).read().strip().split('\n\n')
    p1_raw = p1.split('\n')[1:]
    p1_cards = [int(x) for x in p1_raw]
    p2_raw = p2.split('\n')[1:]
    p2_cards = [int(x) for x in p2_raw]
    print("-- Pre game config --")
    print("p1's deck: {}".format(p1_cards))
    print("p2's deck: {}".format(p2_cards))

    winner, p1_cards, p2_cards = recursive_combat(p1_cards, p2_cards, 1)
    print("-- Post game results --")
    print("p1's deck: {}".format(p1_cards))
    print("p2's deck: {}".format(p2_cards))

    ans = score(winner, p1_cards, p2_cards)
    print(ans)

def recursive_combat(p1_cards, p2_cards, game_id):
    seen = dict()
    while p1_cards and p2_cards:
        # Before dealing card
        p1_key = cards_to_key(p1_cards)
        p2_key = cards_to_key(p2_cards)
        p1_seen = ((p1_key in seen) and (1 in seen[p1_key]))
        p2_seen = ((p2_key in seen) and (2 in seen[p2_key]))
        
        # avoiding loop, p1 wins
        if p1_seen or p2_seen:
            # here means the game ends
            return 1, p1_cards, p2_cards
        # adding current key to seen
        if p1_key in seen:
            seen[p1_key].append(1)
        else:
            seen[p1_key] = [1]
        if p2_key in seen:
            seen[p2_key].append(2)
        else:
            seen[p2_key] = [2]

        # draw cards from top
        p1_dr = p1_cards.pop(0)
        p2_dr = p2_cards.pop(0)

        if p1_dr <= len(p1_cards) and p2_dr <= len(p2_cards):
            new_p1_cards = p1_cards[:p1_dr].copy()
            new_p2_cards = p2_cards[:p2_dr].copy()
            win, new_p1_cards, new_p2_cards = recursive_combat(new_p1_cards, new_p2_cards, game_id + 1)
        else:
            if p1_dr > p2_dr:
                win = 1
            else:
                win = 2

        # winner takes cards
        if win == 1:
            p1_cards.append(p1_dr)
            p1_cards.append(p2_dr)
        elif win == 2:
            p2_cards.append(p2_dr)
            p2_cards.append(p1_dr)

    if p1_cards:
        winner = 1
    else:
        winner = 2
    return winner, p1_cards, p2_cards



def cards_to_key(cards):
    return tuple(cards)

# calculate score based on winner and their cards
def score(winner, p1_cards, p2_cards):
    if winner == 1:
        hands = p1_cards
    else:
        hands = p2_cards
    ans = 0
    mul = 1
    for val in reversed(hands):
        ans += val * mul
        mul += 1
    return ans





if __name__ == "__main__":
    main()
