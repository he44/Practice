class Solution:
    def freqAlphabets(self, s: str) -> str:
        #  let's start from the end
        #  if it's #, the preceding two numbers must be grouped
        #  if it's number, it's a single char
        ans = ""
        size = len(s)
        i = size-1
        while i >= 0:
            #  'j' to 'z'
            if s[i] == "#":
                #  grab the preceding two-digits
                idx = int(s[i-2:i])
                char = chr(ord('j') + idx-10)
                ans += char
                i -= 3
            else:
                idx = int(s[i])
                char = chr(ord('a') + idx - 1)
                ans += char
                i -= 1
        return ans[::-1]
        


def main():
    s = Solution()
    input_s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    #input_s = "25#"
    input_s = "10#11#12"
    output = s.freqAlphabets(input_s)
    print(output)


if __name__ == "__main__":
    main()
