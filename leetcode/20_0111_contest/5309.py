"""
1319/5309. Number of Operations to Make Network Connected

1. First get connceted component of this netwrok, via DFS


Note:

while looking at this problem, I had this concern:

what if we remove this cable and cause the previously connceted part to become disconnected

Notice how this case is actually covreed by "if len(connections) < n - 1"

Assuming we have this connected component of k nodes, 

if removing one edge disconnects them, that means there are only (k-1) edges in this cc originally (should be able to prove this)

Now let's assume we have this k-node cc and another lonely node, 

assuming adding one edge between lonely node and any other node will break the cc

==> there are only (k-1) edges in the cc

==> there are only (k-1) edges in the network, but (k+1) nodes, 

==> covered by the if statement

(Using induction, should be able to generalize this ?)

"""

class Solution:
    def makeConnected(self, n: int, connections) -> int:
        #  simple case, not enough cables
        if len(connections) < n - 1:
            return -1

        #  Convert connections to adjacency list
        neighbors = [ [] for x in range(n)]
        for edge in connections:
            u,v = edge
            neighbors[u].append(v)
            neighbors[v].append(u)
        #print("Neighbors, ", neighbors)

        #  https://www.youtube.com/watch?v=xPO51Cn7gag
        #  so smart

        #  set vs list (?) 
        #  according to this link: https://stackoverflow.com/questions/2831212/python-sets-vs-lists#2831242 
        #  it's faster to check if an item is in a set than to check if an item is in a list?
        #  but set only allows unique objects
        visited = set()

        #  this way to find out number of connected components is so cool
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in neighbors[node]:
                dfs(neighbor)
            return 1

        nbComponents = 0
        for i in range(n):
            nbComponents += dfs(i)

        #  now let's count cables
        return nbComponents - 1


            
                

def main():
    s = Solution()
    inputs = [
        (4, [[0,1],[0,2],[1,2]]),
        (6, [[0,1],[0,2],[0,3],[1,2],[1,3]]),
        (6, [[0,1],[0,2],[0,3],[1,2]]),
        (5, [[0,1],[0,2],[3,4],[2,3]])
    ]
    for case in inputs:
        output = s.makeConnected(*case)
        print(output)

if __name__ == "__main__":
    main()
        
