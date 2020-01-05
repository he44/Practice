"""
Problem 1310 XOR Queries of a Subarray
# 5304 during contest

Properties of XOR:

a ^ a = 0
0 ^ a = a
a ^ a ^ b = 0 ^ b = b

let a = arr[1] ^ ... arr[i-1] 
let b = arr[i] ^ ... arr[j]
a ^ a ^ b = (arr[1] ^ ... arr[i-1]) ^ (arr[1] ^ ... ^ arr[j]) = arr[i] ^ ... ^ arr[j]

let p[i] = arr[0] ^ ... ^ arr[i]

"""


class Solution:
    #  Get an array storing partial results
    def xorQueries(self, arr, queries):
        size = len(arr)
        #  prefix xor
        p = [0 for x in range(size)]
        p[0] = arr[0]
        for i in range(1, size):
            p[i] = arr[i] ^ p[i-1]
        print(p)
        #  query
        output = []
        for l, r in queries:
            if l == 0:
                output.append(p[r])
            else:
                output.append(p[l-1] ^ p[r])
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
