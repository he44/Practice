class Solution:
    def makeConnected(self, n: int, connections) -> int:
        #  Find all connected component
        label = [-1 for x in range(n)]
        used = 0
        for edge in connections:
            a, b = edge
            if label[a] == -1 and label[b] == -1:
                label[a] = used
                label[b] = used
                used += 1
            elif label[b] == -1:
                label[b] = label[a]
            elif label[a] == -1:
                label[a] = label[b]
            else:
                if label[a] != label[b]:
                    to_replcae = label[a]
                    for x in range(n):
                        if label[x] == to_replcae:
                            label[x] = label[b]
        cc = {}
        for label_val in label:
            if label_val not in cc:
                cc[label_val] = 1
            else:
                cc[label_val] += 1
                
        # simple case, all connected
        if len(cc) == 1:
            return 0

        #  we need number of cc
        num_cc = len(cc) - 1 + cc[-1]
        #  total edges - 
        spare = len(connections) - (n - num_cc)

        if spare >= num_cc - 1:
            return num_cc - 1
        else:
            return -1


        # "redundant edges" in each connected componnet?

        
                

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
        
