def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1.txt"
    rules = open(in_fname).read().strip().split('.\n')
    print(len(rules))
    edges = {}
    build_graph(rules, edges)
    for item in edges:
        print("{} can be found in {}".format(item, edges[item]))

    # starting from "shiny gold"
    cur = "shiny gold"
    target = cur
    reachable = set()
    stack = [cur]
    while stack:
        cur = stack.pop()
        if cur != target:
            reachable.add(cur)
        if cur not in edges:
            continue
        for neighbor in edges[cur]:
            if neighbor not in reachable:
                stack.append(neighbor)
    print(len(reachable))
    print("These bags work: {}".format(reachable))


def build_graph(rules, edges):
    for rule in rules:
        src, dst = rule.split(' contain ')
        # no edge
        if dst.find('no other') != -1:
            continue
        src_color = ' '.join(src.split(" ")[:-1])
        dst_bags = dst.split(', ')
        dst_colors = []
        for bag in dst_bags:
            color = ' '.join(bag.split(' ')[1:-1])
            dst_colors.append(color)
        for dst_color in dst_colors:
            if dst_color not in edges:
                edges[dst_color] = [src_color]
            else:
                edges[dst_color].append(src_color)



if __name__ == "__main__":
    main()
