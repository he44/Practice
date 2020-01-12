class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cur_res = a | b
        if cur_res == c:
            return 0
        ##print(cur_res, c)
        # if 1 needs to become 0, 2 flips
        # if 0 needs to become 1, 1 flip
        ab = "{0:b}".format(cur_res)
        c = "{0:b}".format(c)
        d = "{0:b}".format(a & b)
        #  need to zero pad the other one
        len_ab = len(ab)
        len_c = len(c)
        len_d = len(d)
        size = max(len_ab, len_c, len_d)
        pad_ab = ['0' for x in range(size)]
        pad_c = ['0' for x in range(size)]
        pad_d = ['0' for x in range(size)]

        for i in range(0, len_ab):
            pad_ab[i + size - len_ab] = ab[i]

        for i in range(0, len_c):
            pad_c[i + size - len_c] = c[i]

        for i in range(0, len_d):
            pad_d[i + size - len_d] = d[i]

        """
        print("A or B is %s"%pad_ab)
        print("A and B is %s"%pad_d)
        print("C is %s"%pad_c)
        """

        flips = 0
        for i in range(size):
            #  no flip
            if pad_ab[i] == pad_c[i]:
                continue
            if pad_ab[i] == '1' and pad_c[i] == '0':
                if pad_d[i] == '1':
                    flips += 2
                else:
                    flips += 1
            #  must toggle both from 0 to 1
            if pad_ab[i] == '0' and pad_c[i] == '1':
                flips += 1
            #print("i, flips", i, flips)
        return flips

def main():
    s = Solution()
    inputs = [(2,6,5)]
    inputs = [(2,6,5), (4,2,7), (1,2,3), (8,3,5)]
    for input_nums in inputs:
        output = s.minFlips(*input_nums)
        print(output)

if __name__ == "__main__":
    main()
        
