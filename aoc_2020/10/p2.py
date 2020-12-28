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
    ans = count_paths(start, end, edges)
    print(ans)


def count_paths(start, end, edges):
    ans = [0]
    visited = {item: False for item in edges}
    def backtrack(cur, visited):
        visited[cur] = True
        if cur == end:
            ans[0] += 1
        else:
            for neighbor in edges[cur]:
                if neighbor not in edges:
                    continue
                if not visited[neighbor]:
                    backtrack(neighbor, visited)
        visited[cur] = False
    backtrack(start, visited)
    return ans[0]

def build_graphs(target, nodes, start=0):
    edges = dict()
    edges[start] = [start + i for i in range(1,4)]
    edges[target] = [target - i for i in range(1,4)]
    for node in nodes:
        edges[node] = [node - i for i in range(1,4)]
    return edges


if __name__ == "__main__":
    main()
