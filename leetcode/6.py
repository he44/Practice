class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_char = len(s)
        if num_char == 0 or num_char == 1 or numRows == 1:
            return s
        len_group = 2 * numRows - 2
        #  number of groups
        num_group = num_char // len_group + 1
        print(num_group)
        #  fill in each group
        groups = [["" for x in range(2 * numRows - 2)] for y in range(num_group)]
        for gi in range(num_group):
            for ci in range(len_group):
                si = gi * len_group + ci
                if si < num_char:
                    groups[gi][ci] = s[si]
        #print(groups)
        #  convert from group to string
        #  build this placeholder
        group_width = len_group - numRows + 1
        width = num_group * group_width
        height = numRows
        matrix = [["" for x in range(width)] for y in range(height)]
        #  go over group and fill in matrix
        for gi in range(num_group):
            for ci in range(len_group):
                row = 0
                col = 0
                if ci < numRows:
                    row = ci
                    col = gi * group_width
                else:
                    row = 2 * numRows - ci -2
                    col = gi * group_width + (ci - numRows + 1)
                matrix[row][col] = groups[gi][ci]
        #  get row and col number from gi and ci
        #  row = ci if ci < numRows
        #  row = 2 * numRows - ci - 1 if ci >= numRows
        #  col = group_width * gi if ci < numRows
        #  col = group_width * gi + (ci - numRows + 1) if ci >= numRows
        #  Generate output string
        out_str = ""
        for row in range(height):
            for col in range(width):
                out_str += matrix[row][col]
        return out_str
        

def main():
    s = Solution()
    """
    input_str = "PAYPALISHIRING"
    input_row = 4
    """
    input_str = "AB"
    input_row = 1
    output_str = s.convert(input_str, input_row)
    print(output_str)

if __name__ == "__main__":
    main()


"""
PAYPALISHIRING

P     A

A  P  L

Y     I

Assuming there are n rows

zig zag pattern is 

col 0 has n characters

col 1~(n-2) has only 1 character

each group has (n-1) cols, n + (n-2) = (2n - 2) characters

"""
    
