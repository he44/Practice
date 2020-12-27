def main():
    in_fname = "i1_eg.txt"
    in_fname = "i2_eg.txt"
    in_fname = "i1.txt"
    rules = open(in_fname).read().strip().split('.\n')
    print(len(rules))
    edges = {}
    build_graph(rules, edges)
    for item in edges:
        print("{} contains {}".format(item, edges[item]))

    # starting from "shiny gold"
    cur = "shiny gold"
    target = cur
    reachable = set()
    stack = [(cur, 1)]

    total = get_number(cur, edges)
    print(total - 1) # total counted for the "shiny gold" itself


def get_number(start, edges):
    ans = 1
    if start in edges:
        for neighbor, num in edges[start]:
            ans += num * get_number(neighbor, edges)
    return ans



# for part 2, let's revert the direction of all the edges
def build_graph(rules, edges):
    for rule in rules:
        src, dst = rule.split(' contain ')
        src_color = ' '.join(src.split(" ")[:-1])
        # no edge
        if dst.find('no other') != -1:
            continue
        dst_bags = dst.split(', ')
        dst_colors = []
        for bag in dst_bags:
            info = bag.split(' ')
            num = int(info[0])
            color = ' '.join(info[1:-1])
            dst_colors.append((color, num))
        if src_color not in edges:
            edges[src_color] = []
        for dst_color in dst_colors:
            edges[src_color].append(dst_color)



if __name__ == "__main__":
    main()
