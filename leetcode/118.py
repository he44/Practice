"""
118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

class Solution:
    def generate(self, numRows: int):
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        """
        """
        output[0] = [1]
        output[1] = [1,1]
        """
        output = [[] for n in range(numRows)]
        for r in range(numRows):
            # first
            output[r].append(1)
            for c in range(1, r):
                print("r = %d, c = %d"%(r,c))
                output[r].append(output[r-1][c-1] + output[r-1][c])
            # last
            if r >= 1:
                output[r].append(1)
        return output



def main():
    s = Solution()
    input_nr = 5
    output = s.generate(input_nr)
    print(output)

if __name__ == "__main__":
    main()
