class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split(' ')
        keys = []
        for i in range(len(words)):
            keys.append((len(words[i]), i))
        sl, sw = zip(*(sorted(zip(keys, words))))
        sw = list(sw)
        sw[0] = sw[0][0].upper() + sw[0][1:]
        return ' '.join(sw)


def main():
    s = Solution()
    s.arrangeWords("Leetcode is cool")
    s.arrangeWords("Keep calm and code on")
    s.arrangeWords("To be or not to be")

        
if __name__ == "__main__":
    main()
