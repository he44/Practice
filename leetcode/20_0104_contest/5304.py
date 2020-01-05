class Solution:
    #  Get an array storing partial results
    def xorQueries(self, arr, queries):
        def recursion_xor(i, j):
            #  Base case
            if store[i][j] is not None:
                return store[i][j]
            if i == j:
                return arr[i]
            if i == j - 1:
                return arr[i] ^ arr[j]
            #  Recursoin
            ans =  arr[i] ^ recursion_xor(i+1, j-1) ^ arr[j]
            store[i][j] = ans
            return ans
        
        total = len(arr)
        #  store[i][j] denote arr[i] xor .... xor arr[j]
        store = [[None for x in range(total)] for y in range(total)]
        output = []
        #  go through queries
        for pair in queries:
            #  compute
            if store[pair[0]][pair[1]] is not None:
                output.append(store[pair[0]][pair[1]])
            else:
                ans = recursion_xor(pair[0], pair[1])
                store[pair[0]][pair[1]] = ans
                output.append(ans)
        return output
                

def main():
    s = Solution()
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]

    arr = [4,8,2,10]
    queries = [[2,3],[1,3],[0,0],[0,3]]

    output = s.xorQueries(arr, queries)
    print(output)

if __name__ == "__main__":
    main()
