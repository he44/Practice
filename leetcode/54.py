"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.
"""
"""  Example
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        seen = [[False for c in range(n)] for r in range(m)]

        steps = [(0,1), (1,0), (0,-1), (-1,0)]
        
        #  let d denote the direction from previous node
        #  d = 0(right), 1 (down), 2 (left), 3(up)
        def traverse(r, c, m, n, d):
            seen[r][c] = True
            output.append(matrix[r][c])
            #  start from checking direction d
            direc_to_check = [(d+x)%4 for x in range(4)]
            for direc in direc_to_check:
                updates = steps[direc]
            
                new_r = updates[0] + r
                new_c = updates[1] + c
                if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and seen[new_r][new_c] == False:
                    traverse(new_r, new_c, m, n, direc)
                    return

        output = []
        traverse(0,0,m,n,0)
        return output
        
    



def main():
    s = Solution()
    """
    input_m = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    """
    input_m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    input_m = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    input_m = [ [ 1,2,3] ]
    input_m = [
        [1],
        [2],
        [3]
    ]
    output_m = s.spiralOrder(input_m)
    print(output_m)

if __name__ == "__main__":
    main()

    
        
