def main():
    in_fname = "i1_eg.txt"
    in_fname = "i1_eg_2.txt"
    in_fname = "i1.txt"
    lines = open(in_fname).read().strip().split('\n')
    output_joltages = [int(x) for x in lines]
    device_out = max(output_joltages) + 3

    # build a graph and then count the number of paths to device_out?
    edges = build_graphs(device_out, output_joltages)

    print(edges)
    # if we are using all adapters, I can just sort and compute
    chains = sorted(output_joltages)

    # find number of paths between start and end
    start = device_out
    end = 0
    # let counts[start] store the number of arrangements from start to end
    # build it "top down"
    counts = dict()
    count(start, end, edges, counts)
    print(counts[start])


def count(cur, end, edges, counts):
    if cur == end:
        return 1
    if cur in counts:
        return counts[cur]
    ans = 0
    for neighbor in edges[cur]:
        if neighbor in edges:
            ans += count(neighbor, end, edges, counts)
    counts[cur] = ans
    return ans


def build_graphs(target, nodes, start=0):
    edges = dict()
    edges[start] = [start + i for i in range(1,4)]
    edges[target] = [target - i for i in range(1,4)]
    for node in nodes:
        edges[node] = [node - i for i in range(1,4)]
    return edges
    

if __name__ == "__main__":
    main()
