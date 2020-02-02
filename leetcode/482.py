class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #  get rid of the old dash
        old_groups = S.split('-')
        all_chars = ''.join(old_groups).upper()
        #  check the first group's length
        size = len(all_chars)
        len_1 = size % K
        if len_1 == 0:
            len_1 = K
        new_format = all_chars[0:len_1]
        for i in range(len_1, size, K):
            new_format += ('-' + all_chars[i:i+K])
        return new_format
            

def main():
    s = Solution()
    inputs = [
        ("5F3Z-2e-9-w", 4),
        ("2-5g-3-J", 2)
    ]
    for S, K in inputs:
        out = s.licenseKeyFormatting(S, K)
        print(out)


if __name__ == "__main__":
    main()
        
