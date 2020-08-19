from typing import *

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set(['a','e','i','o','u'])
        words = S.split()
        ans = []
        for wi in range(len(words)):
            word = words[wi]
            start = word[0]
            # consonant remove and append
            if start.lower() not in vowels:
                new_word = word[1:] + word[0] + 'ma'
            else:
                new_word = word + 'ma'
            new_word = new_word + 'a' * (wi + 1)
            ans.append(new_word)
        return ' '.join(ans)

cases = [
    "I speak Goat Latin",
    "The quick brown fox jumped over the lazy dog",
    ""
]

sol = Solution()
for case in cases:
    print(sol.toGoatLatin(case))


